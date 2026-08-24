import asyncio
from datetime import datetime, timedelta
from typing import Callable, Dict
import structlog

logger = structlog.get_logger()

class SchedulerService:
    def __init__(self):
        self._tasks: Dict[str, asyncio.Task] = {}
        self._running = False
        self._jobs: Dict[str, dict] = {}

    async def start(self):
        self._running = True
        logger.info("scheduler_started")


        self._schedule("inventory_reorder_check", self._check_reorder_points, hours=6)
        self._schedule("invoice_reminder", self._send_invoice_reminders, hours=24)
        self._schedule("ai_daily_digest", self._generate_ai_digest, hours=24)
        self._schedule("system_health_check", self._system_health_check, minutes=5)

    def _schedule(self, name: str, coro: Callable, minutes: int = 0, hours: int = 0):
        interval = (hours * 3600) + (minutes * 60)
        if interval <= 0:
            interval = 3600

        async def loop():
            while self._running:
                try:
                    await coro()
                except Exception as e:
                    logger.error("scheduled_task_failed", task=name, error=str(e))
                await asyncio.sleep(interval)

        self._tasks[name] = asyncio.create_task(loop())
        self._jobs[name] = {"interval": interval, "last_run": None, "status": "running"}

    async def _check_reorder_points(self):
        logger.info("task_reorder_check")
        await event_bus.publish("inventory.reorder_check", {"timestamp": datetime.utcnow().isoformat()})

    async def _send_invoice_reminders(self):
        logger.info("task_invoice_reminders")
        await event_bus.publish("finance.invoice_reminders", {"timestamp": datetime.utcnow().isoformat()})

    async def _generate_ai_digest(self):
        logger.info("task_ai_digest")
        await event_bus.publish("ai.daily_digest", {"timestamp": datetime.utcnow().isoformat()})

    async def _system_health_check(self):
        logger.debug("task_health_check")

    async def stop(self):
        self._running = False
        for name, task in self._tasks.items():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        logger.info("scheduler_stopped")

    def is_running(self) -> bool:
        return self._running

    def get_jobs(self) -> Dict:
        return self._jobs

scheduler_service = SchedulerService()