import json
import asyncio
from typing import Callable, Dict, List, Any
import aio_pika
from aio_pika.abc import AbstractIncomingMessage
from app.config import settings
import structlog

logger = structlog.get_logger()

class EventBus:
    def __init__(self):
        self._connection = None
        self._channel = None
        self._exchange = None
        self._handlers: Dict[str, List[Callable]] = {}
        self._queues: Dict[str, aio_pika.Queue] = {}

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
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
            )
            await self._exchange.publish(message, routing_key=event_type)
            logger.debug("event_published", type=event_type)
        except Exception as e:
            logger.warning("event_publish_failed", error=str(e))

    async def subscribe(self, event_type: str, handler: Callable):
        if not self._channel:
            return
        queue_name = f"queue.{event_type}"
        queue = await self._channel.declare_queue(queue_name, durable=True)
        await queue.bind(self._exchange, routing_key=event_type)
        
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)
        
        self._queues[event_type] = queue
        
        async def process_message(message: AbstractIncomingMessage):
            async with message.process():
                try:
                    payload = json.loads(message.body)
                    # Extract event type from routing key or payload
                    evt_type = message.routing_key or payload.get("event_type", "unknown")
                    for h in self._handlers.get(evt_type, []):
                        asyncio.create_task(h(payload))
                except Exception as e:
                    logger.error("event_handler_error", error=str(e))
        
        await queue.consume(process_message)

    async def consume(self, queue_name: str, handler: Callable):
        """Consume messages from a specific queue and forward to handler"""
        if not self._channel:
            logger.warning("Cannot consume: channel not available")
            return
        
        queue = await self._channel.declare_queue(queue_name, durable=True)
        await queue.bind(self._exchange, routing_key="erp.#")
        
        async def process_message(message: AbstractIncomingMessage):
            async with message.process():
                try:
                    payload = json.loads(message.body)
                    event_type = payload.get("event_type", "unknown")
                    await handler(event_type, payload)
                except Exception as e:
                    logger.error("consume_handler_error", error=str(e))
        
        await queue.consume(process_message)
        logger.info(f"Consuming messages from queue: {queue_name}")

    async def health(self):
        if not self._connection or self._connection.is_closed:
            return "disconnected"
        return "connected"

    async def disconnect(self):
        if self._connection and not self._connection.is_closed:
            await self._connection.close()
        logger.info("event_bus_disconnected")

event_bus = EventBus()