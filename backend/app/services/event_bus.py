"""Async Event Bus with RabbitMQ backend and topic-based routing."""
import json
import asyncio
from typing import Callable, Dict, List
import aio_pika
from app.config import settings
import structlog

logger = structlog.get_logger()

class EventBus:
    def __init__(self):
        self._connection = None
        self._channel = None
        self._exchange = None
        self._handlers: Dict[str, List[Callable]] = {}

    async def connect(self):
        try:
            self._connection = await aio_pika.connect_robust(str(settings.RABBITMQ_URL))
            self._channel = await self._connection.channel()
            self._exchange = await self._channel.declare_exchange(
                settings.RABBITMQ_EXCHANGE, aio_pika.ExchangeType.TOPIC
            )
            logger.info("event_bus_connected")
        except Exception as e:
            logger.warning("event_bus_connection_failed", error=str(e))

    async def publish(self, event_type: str, payload: dict):
        if not self._exchange:
            return
        try:
            message = aio_pika.Message(
                body=json.dumps(payload, default=str).encode(),
                content_type="application/json",
            )
            await self._exchange.publish(message, routing_key=event_type)
            logger.debug("event_published", type=event_type)
        except Exception as e:
            logger.warning("event_publish_failed", error=str(e))

    async def subscribe(self, event_type: str, handler: Callable):
        if not self._channel:
            return
        queue = await self._channel.declare_queue(exclusive=True)
        await queue.bind(self._exchange, routing_key=event_type)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    try:
                        payload = json.loads(message.body)
                        for h in self._handlers.get(event_type, []):
                            asyncio.create_task(h(payload))
                    except Exception as e:
                        logger.error("event_handler_error", error=str(e))

    async def health(self):
        if not self._connection or self._connection.is_closed:
            return "disconnected"
        return "connected"

    async def disconnect(self):
        if self._connection and not self._connection.is_closed:
            await self._connection.close()
        logger.info("event_bus_disconnected")

event_bus = EventBus()
