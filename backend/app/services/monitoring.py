"""System metrics collection with Prometheus-compatible output."""
import time
import psutil
from typing import Dict
import structlog

logger = structlog.get_logger()
_start_time = time.time()

class MetricsCollector:
    def __init__(self):
        self._running = False
        self._metrics = {}

    def start(self):
        self._running = True
        logger.info("metrics_collector_started")

    def stop(self):
        self._running = False

    async def get_metrics(self) -> Dict:
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        return {
            "uptime_seconds": int(time.time() - _start_time),
            "cpu_percent": psutil.cpu_percent(interval=0.1),
            "memory": {
                "used_mb": mem.used // (1024 * 1024),
                "total_mb": mem.total // (1024 * 1024),
                "percent": mem.percent,
                "available_mb": mem.available // (1024 * 1024),
            },
            "disk": {
                "used_gb": disk.used // (1024**3),
                "total_gb": disk.total // (1024**3),
                "percent": disk.percent,
            },
            "network": {
                "connections": len(psutil.net_connections()),
            },
            "timestamp": time.time(),
        }

metrics_collector = MetricsCollector()
