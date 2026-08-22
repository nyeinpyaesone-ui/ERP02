"""
Workers Module Initialization
"""
from .event_worker import EventWorker, main as event_worker_main

__all__ = ["EventWorker", "event_worker_main"]
