"""
Enterprise Event Bus - RabbitMQ Implementation
Handles asynchronous communication between ERP modules (Finance, HR, SCM, Manufacturing, CRM)
Ensures reliable delivery, persistence, and dead-letter handling for critical business events.
"""
import asyncio
import aio_pika
from aio_pika import Message, ExchangeType, DeliveryMode
from typing import Any, Dict, Optional, Callable
import json
import logging
from datetime import datetime
from backend.app.core.config import settings

logger = logging.getLogger(__name__)

class EnterpriseEventBus:
    def __init__(self):
        self.connection: Optional[aio_pika.Connection] = None
        self.channel: Optional[aio_pika.Channel] = None
        self.exchanges: Dict[str, aio_pika.Exchange] = {}
        self._reconnect_delay = 5
        self.is_connected = False

    async def connect(self):
        """Establish connection to RabbitMQ with retry logic"""
        retries = 10
        while retries > 0:
            try:
                self.connection = await aio_pika.connect_robust(
                    settings.RABBITMQ_URL,
                    client_properties={"connection_name": "erp_core_service"}
                )
                self.channel = await self.connection.channel()
                await self.channel.set_qos(prefetch_count=100)

                # Declare core domain exchanges for explicit module separation
                domains = ["finance", "hrm", "scm", "manufacturing", "crm"]
                for domain in domains:
                    exchange = await self.channel.declare_exchange(
                        f"erp.{domain}",
                        ExchangeType.TOPIC,
                        durable=True
                    )
                    self.exchanges[domain] = exchange

                self.is_connected = True
                logger.info("Enterprise Event Bus connected successfully")
                return
            except Exception as e:
                retries -= 1
                logger.error(f"RabbitMQ connection failed: {e}. Retries left: {retries}")
                await asyncio.sleep(self._reconnect_delay)
        
        raise ConnectionError("Failed to connect to RabbitMQ after multiple attempts")

    async def publish_event(self, domain: str, event_type: str, payload: Dict[str, Any], mandatory: bool = True):
        """
        Publish event to specific domain exchange.
        Routing Key Format: {domain}.{entity}.{action} 
        Examples: finance.journal.posted, hrm.payroll.processed, scm.inventory.updated
        """
        if not self.is_connected or domain not in self.exchanges:
            logger.warning(f"Event Bus not connected or unknown domain: {domain}")
            return

        # Wrap payload with metadata for audit trail
        enriched_payload = {
            "event_id": settings.INSTANCE_ID,
            "timestamp": datetime.utcnow().isoformat(),
            "domain": domain,
            "event_type": event_type,
            "payload": payload
        }

        message = Message(
            body=json.dumps(enriched_payload).encode(),
            delivery_mode=DeliveryMode.PERSISTENT,
            content_type="application/json",
            headers={"erp_version": "2.0", "source": "core_service"}
        )

        routing_key = f"{domain}.{event_type}"
        try:
            await self.exchanges[domain].publish(message, routing_key=routing_key, mandatory=mandatory)
            logger.info(f"Event published: {routing_key}")
        except Exception as e:
            logger.error(f"Failed to publish event {routing_key}: {e}")
            raise

    async def subscribe(self, domain: str, queue_name: str, callback: Callable, routing_key: str = "#"):
        """
        Subscribe to domain events.
        Creates durable queue with Dead Letter Exchange (DLX) support for failed messages.
        """
        if not self.is_connected or domain not in self.exchanges:
            raise ConnectionError("Event Bus not connected")

        # Declare Dead Letter Exchange and Queue
        dlx_name = f"{queue_name}.dlx"
        dlx_exchange = await self.channel.declare_exchange(dlx_name, ExchangeType.DIRECT, durable=True)
        dlx_queue = await self.channel.declare_queue(f"{queue_name}.dead_letter", durable=True)
        await dlx_queue.bind(dlx_exchange, routing_key="dead_letter")

        # Declare main queue with DLX argument
        queue = await self.channel.declare_queue(
            queue_name,
            durable=True,
            arguments={"x-dead-letter-exchange": dlx_name}
        )

        await queue.bind(self.exchanges[domain], routing_key=routing_key)
        logger.info(f"Subscribed to {domain} events on queue '{queue_name}'")

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    try:
                        data = json.loads(message.body.decode())
                        await callback(data)
                    except Exception as e:
                        logger.error(f"Error processing message in {queue_name}: {e}")
                        # Message automatically rejected and sent to DLX

    async def close(self):
        if self.connection:
            await self.connection.close()
            self.is_connected = False
            logger.info("Event Bus connection closed")

# Global singleton instance
event_bus = EnterpriseEventBus()
