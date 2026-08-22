"""AI Agent System - Ollama-powered with 15+ Specialized Skills"""
import asyncio
import json
import re
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Callable
import structlog

import httpx

from app.config import settings

logger = structlog.get_logger()


class OllamaClient:
    """Async Ollama client with connection pooling and retry logic."""

    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.timeout = settings.OLLAMA_TIMEOUT
        self._client = None
        self._semaphore = asyncio.Semaphore(settings.AI_MAX_CONCURRENT)

    async def _get_client(self):
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                timeout=httpx.Timeout(self.timeout),
                limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
            )
        return self._client

    async def generate(self, model, prompt, system=None, temperature=None, max_tokens=None, format=None, stream=False):
        async with self._semaphore:
            client = await self._get_client()
            payload = {
                "model": model, "prompt": prompt, "stream": stream,
                "options": {
                    "temperature": temperature or settings.AI_TEMPERATURE,
                    "num_predict": max_tokens or settings.AI_MAX_TOKENS,
                    "top_p": settings.AI_TOP_P,
                },
            }
            if system:
                payload["system"] = system
            if format:
                payload["format"] = format

            for attempt in range(3):
                try:
                    resp = await client.post(f"{self.base_url}/api/generate", json=payload, timeout=settings.AI_REQUEST_TIMEOUT)
                    resp.raise_for_status()
                    data = resp.json()
                    return {
                        "text": data.get("response", ""),
                        "model": model,
                        "tokens": data.get("eval_count", 0),
                        "prompt_tokens": data.get("prompt_eval_count", 0),
                        "done": data.get("done", True),
                    }
                except Exception as e:
                    if attempt == 2:
                        logger.error("ollama_request_failed", error=str(e), model=model)
                        raise
                    await asyncio.sleep(2 ** attempt)

    async def embed(self, model, text):
        client = await self._get_client()
        resp = await client.post(f"{self.base_url}/api/embeddings", json={"model": model, "prompt": text}, timeout=30)
        resp.raise_for_status()
        return resp.json().get("embedding", [])

    async def list_models(self):
        client = await self._get_client()
        resp = await client.get(f"{self.base_url}/api/tags", timeout=10)
        resp.raise_for_status()
        return [m["name"] for m in resp.json().get("models", [])]

    async def health(self):
        try:
            models = await self.list_models()
            return "healthy" if models else "no_models"
        except Exception:
            return "unhealthy"

    async def close(self):
        if self._client and not self._client.is_closed:
            await self._client.aclose()

ollama = OllamaClient()


@dataclass
class AgentContext:
    tenant_id: str
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4())[:12])


class BaseAgent(ABC):
    name = "base_agent"
    description = "Base agent"
    default_model = "llama3.1"

    def __init__(self):
        self.logger = logger.bind(agent=self.name)

    async def run(self, skill_name, input_data, context, model=None):
        start = datetime.utcnow()
        model = model or self.default_model
        self.logger.info("agent_run_start", skill=skill_name, tenant=context.tenant_id, trace=context.trace_id)

        try:
            skill = self._get_skill(skill_name)
            result = await skill(input_data, context, model)
            asyncio.create_task(self._record_run(context, skill_name, model, result, start))
            self.logger.info("agent_run_complete", skill=skill_name, trace=context.trace_id)
            return result
        except Exception as e:
            self.logger.error("agent_run_failed", skill=skill_name, error=str(e), trace=context.trace_id)
            asyncio.create_task(self._record_run(context, skill_name, model, {"error": str(e)}, start, failed=True))
            raise

    @abstractmethod
    def _get_skill(self, skill_name):
        pass

    async def _record_run(self, context, skill, model, result, start, failed=False):
        try:
            from app.db.session import AsyncSessionLocal
            from app.db.models import AIAgentRun
            async with AsyncSessionLocal() as db:
                run = AIAgentRun(
                    tenant_id=context.tenant_id,
                    agent_name=self.name,
                    skill_used=skill,
                    input_summary=str(result.get("input", "")[:500]),
                    output_summary=str(result.get("output", "")[:500]) if not failed else None,
                    model_used=model,
                    tokens_used=result.get("tokens", 0),
                    cost_usd=Decimal(str(result.get("cost", 0))),
                    execution_time_ms=int((datetime.utcnow() - start).total_seconds() * 1000),
                    status="error" if failed else "success",
                    error_message=str(result.get("error", ""))[:500] if failed else None,
                    triggered_by=context.user_id,
                )
                db.add(run)
                await db.commit()
        except Exception:
            pass


class ERPAIAgent(BaseAgent):
    name = "erp_ai_agent"
    description = "AI agent for ERP operations"
    default_model = "llama3.1"
    SKILLS = {}

    def __init__(self):
        super().__init__()
        self._register_all_skills()

    def _register_all_skills(self):
        skills = [
            self._inventory_forecast, self._inventory_reorder_optimizer, self._demand_pattern_analysis,
            self._lead_scoring, self._churn_prediction, self._sales_forecast,
            self._anomaly_detection, self._cash_flow_forecast, self._invoice_risk_scoring,
            self._timesheet_anomaly_detection, self._leave_optimization,
            self._supplier_risk_assessment, self._po_optimization,
            self._production_efficiency_forecast,
            self._project_risk_assessment,
            self._compliance_document_review,
            self._natural_language_query,
        ]
        for skill in skills:
            self.SKILLS[skill.__name__] = skill

    def _get_skill(self, skill_name):
        if skill_name not in self.SKILLS:
            raise ValueError(f"Unknown skill: {skill_name}. Available: {list(self.SKILLS.keys())}")
        return self.SKILLS[skill_name]

    def _safe_json_parse(self, text):
        patterns = [r'```json\s*(.*?)\s*```', r'```\s*(.*?)\s*```', r'\{.*\}', r'\[.*\]']
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1) if pattern.startswith(r'```') else match.group(0))
                except json.JSONDecodeError:
                    continue
        return {"raw_response": text[:1000], "parse_error": True}

    # INVENTORY
    async def _inventory_forecast(self, data, ctx, model):
        prompt = f"""Predict inventory needs for 30/60/90 days. Sales History: {data.get('sales_history', [])[:60]}
Respond in JSON: {{"forecast_30d": int, "forecast_60d": int, "forecast_90d": int, "confidence": float, "trend": str, "safety_stock_recommendation": int, "reasoning": str}}"""
        resp = await ollama.generate(model=model, prompt=prompt, system="Supply chain AI. Output valid JSON only.", format="json", temperature=0.3)
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    async def _inventory_reorder_optimizer(self, data, ctx, model):
        prompt = f"""Optimize reorder using EOQ/ROP: {json.dumps(data.get('products', []), default=str)[:4000]}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json", temperature=0.3)
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    async def _demand_pattern_analysis(self, data, ctx, model):
        prompt = f"""ABC/XYZ classification: {json.dumps(data.get('sales_data', []), default=str)[:4000]}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    # CRM
    async def _lead_scoring(self, data, ctx, model):
        prompt = f"""Score leads 0-100: {json.dumps(data.get('leads', []), default=str)[:4000]}
JSON: [{{"lead_id": str, "score": int, "tier": str, "reasoning": str, "recommended_action": str}}]"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    async def _churn_prediction(self, data, ctx, model):
        prompt = f"""Predict churn 0-1: {json.dumps(data.get('customers', []), default=str)[:4000]}
JSON: [{{"customer_id": str, "churn_probability": float, "risk_level": str, "warning_signals": [...], "retention_actions": [...]}}]"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    async def _sales_forecast(self, data, ctx, model):
        prompt = f"""Forecast 12-month revenue: {json.dumps(data.get('historical_sales', []), default=str)[:4000]}
JSON: {{"monthly_forecast": [{{"month": str, "revenue": int, "confidence": float}}], "total_forecast": int, "growth_rate": float, "key_drivers": [...]}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    # FINANCE
    async def _anomaly_detection(self, data, ctx, model):
        prompt = f"""Detect financial anomalies: {json.dumps(data.get('transactions', []), default=str)[:4000]}
JSON: {{"anomalies": [{{"transaction_id": str, "type": str, "severity": str, "explanation": str}}], "summary": str}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    async def _cash_flow_forecast(self, data, ctx, model):
        prompt = f"""Forecast 13-week cash flow: {json.dumps(data.get('cash_data', {}), default=str)[:4000]}
JSON: {{"weekly_forecast": [{{"week": str, "inflow": int, "outflow": int, "net": int, "balance": int}}], "minimum_balance_week": str, "risk_periods": [...]}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    async def _invoice_risk_scoring(self, data, ctx, model):
        prompt = f"""Score invoice payment risk 0-1: {json.dumps(data.get('invoices', []), default=str)[:4000]}
JSON: [{{"invoice_id": str, "risk_score": float, "risk_level": str, "expected_payment_date": str, "recommended_action": str}}]"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    # HR
    async def _timesheet_anomaly_detection(self, data, ctx, model):
        prompt = f"""Detect timesheet anomalies: {json.dumps(data.get('timesheets', []), default=str)[:4000]}
JSON: {{"flagged_entries": [{{"timesheet_id": str, "employee": str, "anomaly_type": str, "severity": str, "details": str}}], "summary_stats": {{}}}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    async def _leave_optimization(self, data, ctx, model):
        prompt = f"""Optimize leave approvals: {json.dumps(data.get('leave_requests', []), default=str)[:4000]} Staffing: {json.dumps(data.get('staffing_requirements', {}), default=str)[:2000]}
JSON: {{"approved": [...], "denied": [...], "deferred": [...], "reasoning": str, "alternative_dates": {{}}}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    # PROCUREMENT
    async def _supplier_risk_assessment(self, data, ctx, model):
        prompt = f"""Assess supplier risk 0-1: {json.dumps(data.get('suppliers', []), default=str)[:4000]}
JSON: [{{"supplier_id": str, "risk_score": float, "risk_category": str, "risk_factors": [...], "mitigation_actions": [...]}}]"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    async def _po_optimization(self, data, ctx, model):
        prompt = f"""Optimize purchase orders: {json.dumps(data.get('requirements', []), default=str)[:4000]} Quotes: {json.dumps(data.get('supplier_quotes', []), default=str)[:4000]}
JSON: {{"optimized_pos": [...], "savings_estimate": int, "consolidation_opportunities": [...], "negotiation_talking_points": [...]}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    # MANUFACTURING
    async def _production_efficiency_forecast(self, data, ctx, model):
        prompt = f"""Forecast production efficiency: {json.dumps(data.get('work_orders', []), default=str)[:4000]}
JSON: {{"efficiency_forecast": float, "bottleneck_workstations": [...], "capacity_constraints": [...], "recommended_actions": [...], "schedule_risk": str}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    # PROJECTS
    async def _project_risk_assessment(self, data, ctx, model):
        prompt = f"""Assess project risks: {json.dumps(data.get('projects', []), default=str)[:4000]}
JSON: [{{"project_id": str, "overall_risk": str, "risk_breakdown": {{"schedule": float, "budget": float, "resource": float, "scope": float, "external": float, "quality": float}}, "top_risks": [...], "mitigation_plan": [...]}}]"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    # COMPLIANCE
    async def _compliance_document_review(self, data, ctx, model):
        doc = data.get("document_text", "")[:8000]
        doc_type = data.get("document_type", "policy")
        prompt = f"""Review this {doc_type} for compliance gaps: {doc}
JSON: {{"compliance_score": int, "gaps": [{{"section": str, "issue": str, "severity": str, "recommendation": str}}], "overall_assessment": str, "action_items": [...]}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}

    # GENERAL
    async def _natural_language_query(self, data, ctx, model):
        query = data.get("query", "")
        schema = data.get("schema", "ERP with products, customers, orders, invoices, employees")
        prompt = f"""Convert NL to SQL: Schema: {schema} Query: "{query}"
JSON: {{"sql": str, "summary": str, "suggested_charts": [...], "confidence": float}}"""
        resp = await ollama.generate(model=model, prompt=prompt, format="json")
        return {"output": self._safe_json_parse(resp["text"]), "tokens": resp["tokens"], "cost": round(resp["tokens"] * 0.0001, 6)}


class AIOrchestrator:
    """Central coordinator for all AI agents in the ERP."""

    def __init__(self):
        self.agents = {}
        self._initialized = False

    async def initialize(self):
        self.agents["erp"] = ERPAIAgent()
        self._initialized = True
        logger.info("ai_orchestrator_initialized", agents=list(self.agents.keys()))

    async def execute(self, agent_name, skill, data, context, model=None):
        if not self._initialized:
            raise RuntimeError("Orchestrator not initialized")
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Agent '{agent_name}' not found")
        return await agent.run(skill, data, context, model)

    async def health(self):
        return await ollama.health()

    async def shutdown(self):
        await ollama.close()
        self._initialized = False

ai_orchestrator = AIOrchestrator()
