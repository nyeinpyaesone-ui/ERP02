# AI ERP System v2.0.0-final

> **AI-Native Enterprise Resource Planning** with 15+ Specialized AI Agents, Multi-Tenant Architecture, and Real-Time Intelligence.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI ERP System v2.0.0-final                      │
├─────────────────────────────────────────────────────────────────┤
│  Frontend Layer                                                  │
│  ├─ Admin Portal (Next.js 14)     → http://localhost:3000       │
│  ├─ Client Dashboard (React 18)   → http://localhost:3001       │
│  └─ Nginx Reverse Proxy           → http://localhost:80         │
├─────────────────────────────────────────────────────────────────┤
│  API Layer (FastAPI + Async)                                     │
│  ├─ RESTful API (11 modules)      → http://localhost:8000      │
│  ├─ WebSocket Real-Time Updates                                  │
│  ├─ Rate Limiting & CORS                                         │
│  └─ JWT Authentication + MFA Ready                             │
├─────────────────────────────────────────────────────────────────┤
│  AI Agent Layer (Ollama-powered)                                 │
│  ├─ 15+ Specialized Skills                                       │
│  ├─ Agent Orchestrator with Observability                       │
│  ├─ Cost Tracking per Agent Run                                  │
│  └─ Multi-Model Support (Llama 3.1, Mistral, CodeLlama, Embed)   │
├─────────────────────────────────────────────────────────────────┤
│  Business Logic Layer                                            │
│  ├─ Inventory, CRM, Finance, HR, Procurement, Manufacturing   │
│  ├─ Projects, Compliance, Analytics                            │
│  ├─ Event Bus (RabbitMQ), Cache (Redis), Scheduler            │
│  └─ Audit Logging + Anomaly Detection                           │
├─────────────────────────────────────────────────────────────────┤
│  Data Layer                                                      │
│  ├─ PostgreSQL 16 (Async) with 25+ tables                        │
│  ├─ Multi-Tenant Isolation (Schema/Row Level)                    │
│  └─ JSONB for Flexible Metadata                                  │
├─────────────────────────────────────────────────────────────────┤
│  Infrastructure                                                  │
│  ├─ Docker Compose (10 Services)                                 │
│  ├─ Prometheus + Grafana Monitoring                              │
│  └─ One-Command Deployment Script                                │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

```bash
# 1. Extract the package
unzip ai-erp-final.zip
cd ai-erp-final

# 2. Deploy everything
chmod +x scripts/setup.sh
./scripts/setup.sh

# 3. Access the system
# Admin Portal:     http://localhost:3000
# Client Dashboard: http://localhost:3001
# API Docs:         http://localhost:8000/docs
```

## File Structure (50+ files)

```
ai-erp-final/
├── backend/
│   ├── app/
│   │   ├── main.py                 # Production FastAPI entry point
│   │   ├── config.py               # Pydantic v2 settings
│   │   ├── db/
│   │   │   ├── session.py          # Async SQLAlchemy 2.0
│   │   │   └── models.py           # 25+ comprehensive models
│   │   ├── api/v1/
│   │   │   ├── auth.py             # JWT auth + MFA ready
│   │   │   ├── inventory.py        # Products, stock, AI forecast
│   │   │   ├── crm.py              # Customers, orders, AI scoring
│   │   │   ├── finance.py          # GL, invoices, AI anomaly detection
│   │   │   ├── hr.py               # Employees, timesheets, AI optimization
│   │   │   ├── ai_agents.py        # 15+ skill runner + chat
│   │   │   ├── analytics.py          # Business intelligence
│   │   │   ├── procurement.py        # Suppliers, POs
│   │   │   ├── manufacturing.py      # BOM, work orders
│   │   │   ├── projects.py         # Project management
│   │   │   └── compliance.py       # Document review
│   │   ├── ai/
│   │   │   └── agent_system.py     # Ollama client + 15 skills
│   │   ├── services/
│   │   │   ├── event_bus.py        # RabbitMQ events
│   │   │   ├── cache_manager.py    # Redis caching
│   │   │   ├── scheduler.py        # Background tasks
│   │   │   └── monitoring.py       # System metrics
│   │   └── middleware/
│   │       ├── tenant.py           # Multi-tenant isolation
│   │       ├── audit.py              # Audit logging
│   │       ├── error_handler.py    # Global error handling
│   │       └── request_timing.py     # Performance monitoring
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── admin-portal/               # Next.js 14
│   │   ├── app/
│   │   │   ├── layout.tsx
│   │   │   ├── login/page.tsx
│   │   │   ├── (app)/
│   │   │   │   ├── layout.tsx
│   │   │   │   ├── dashboard/page.tsx
│   │   │   │   ├── inventory/page.tsx
│   │   │   │   ├── ai-agents/page.tsx
│   │   │   │   └── ...
│   │   │   └── globals.css
│   │   ├── components/
│   │   │   ├── layout/sidebar.tsx
│   │   │   ├── layout/header.tsx
│   │   │   ├── ui/card.tsx
│   │   │   ├── ui/badge.tsx
│   │   │   └── ui/button.tsx
│   │   ├── hooks/
│   │   │   └── useAuth.ts
│   │   ├── lib/
│   │   │   ├── api.ts
│   │   │   └── utils.ts
│   │   ├── package.json
│   │   ├── next.config.js
│   │   ├── tailwind.config.ts
│   │   └── tsconfig.json
│   └── client-dashboard/           # React 18 SPA
│       ├── src/
│       │   ├── App.tsx
│       │   ├── index.tsx
│       │   ├── index.css
│       │   ├── pages/
│       │   │   ├── ClientDashboard.tsx
│       │   │   ├── ClientOrders.tsx
│       │   │   ├── ClientInvoices.tsx
│       │   │   ├── ClientProfile.tsx
│       │   │   └── ClientLogin.tsx
│       │   ├── components/
│       │   │   ├── ClientLayout.tsx
│       │   │   └── ui/card.tsx
│       │   └── hooks/
│       ├── public/index.html
│       ├── package.json
│       └── tailwind.config.js
├── infrastructure/
│   ├── docker-compose.yml            # 10 services
│   ├── nginx.conf                    # Reverse proxy config
│   ├── prometheus.yml                # Metrics scraping
│   └── init.sql                      # DB extensions
├── scripts/
│   └── setup.sh                      # One-command deployer
└── README.md
```

## AI Agent Skills (15+)

| Category | Skill | Description |
|----------|-------|-------------|
| **Inventory** | `_inventory_forecast` | Predict stock needs 30/60/90 days |
| | `_inventory_reorder_optimizer` | EOQ/ROP optimization |
| | `_demand_pattern_analysis` | ABC/XYZ classification |
| **CRM** | `_lead_scoring` | Score leads 0-100 |
| | `_churn_prediction` | Predict churn probability |
| | `_sales_forecast` | 12-month revenue forecast |
| **Finance** | `_anomaly_detection` | Detect transaction anomalies |
| | `_cash_flow_forecast` | 13-week cash flow prediction |
| | `_invoice_risk_scoring` | Score payment risk |
| **HR** | `_timesheet_anomaly_detection` | Detect overtime abuse |
| | `_leave_optimization` | Optimize leave scheduling |
| **Procurement** | `_supplier_risk_assessment` | Financial/geopolitical risk |
| | `_po_optimization` | Consolidate & negotiate |
| **Manufacturing** | `_production_efficiency_forecast` | Bottleneck prediction |
| **Projects** | `_project_risk_assessment` | Multi-dimensional risk |
| **Compliance** | `_compliance_document_review` | Regulatory gap analysis |
| **General** | `_natural_language_query` | NL → SQL / insights |

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - JWT login
- `POST /api/v1/auth/refresh` - Token refresh
- `GET /api/v1/auth/me` - Current user

### Inventory
- `GET /api/v1/inventory/products` - List products
- `POST /api/v1/inventory/products` - Create product
- `POST /api/v1/inventory/products/{id}/forecast` - AI forecast
- `POST /api/v1/inventory/stock-movements` - Stock adjustment
- `GET /api/v1/inventory/low-stock` - Low stock alerts
- `GET /api/v1/inventory/dashboard` - KPIs

### CRM
- `GET /api/v1/crm/customers` - List customers
- `POST /api/v1/crm/customers` - Create customer
- `POST /api/v1/crm/customers/{id}/interactions` - Add interaction (AI sentiment)
- `POST /api/v1/crm/ai/lead-scoring` - AI lead scoring
- `POST /api/v1/crm/ai/churn-prediction` - AI churn prediction

### Finance
- `GET /api/v1/finance/accounts` - Chart of accounts
- `POST /api/v1/finance/journal-entries` - Create journal entry
- `POST /api/v1/finance/invoices` - Create invoice
- `POST /api/v1/finance/payments` - Record payment
- `POST /api/v1/finance/ai/anomaly-detection` - AI anomaly detection
- `POST /api/v1/finance/ai/cash-flow-forecast` - AI cash flow

### HR
- `GET /api/v1/hr/employees` - List employees
- `POST /api/v1/hr/employees` - Create employee
- `POST /api/v1/hr/timesheets` - Submit timesheet (AI anomaly check)
- `POST /api/v1/hr/leave-requests` - Request leave
- `POST /api/v1/hr/ai/leave-optimization` - AI leave optimization

### AI Agents
- `GET /api/v1/ai/skills` - List all skills
- `POST /api/v1/ai/run` - Execute any skill
- `POST /api/v1/ai/chat` - Conversational AI
- `GET /api/v1/ai/conversations/{session_id}` - Chat history
- `GET /api/v1/ai/runs/history` - Agent run history
- `GET /api/v1/ai/models` - Available Ollama models

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11, FastAPI, SQLAlchemy 2.0 (Async), Pydantic v2 |
| Database | PostgreSQL 16, Redis 7, RabbitMQ 3 |
| AI Engine | Ollama (Llama 3.1, Mistral, CodeLlama, Nomic Embed) |
| Frontend Admin | Next.js 14, React 18, Tailwind CSS, TanStack Query |
| Frontend Client | React 18, React Router, Tailwind CSS |
| Infrastructure | Docker Compose, Nginx, Prometheus, Grafana |
| Security | JWT, bcrypt, Rate Limiting, Audit Logging, CORS |

## License

MIT License - Open Source Enterprise AI ERP System.
