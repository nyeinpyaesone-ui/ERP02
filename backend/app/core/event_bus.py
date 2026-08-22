"""
Enterprise Event Bus - RabbitMQ Implementation
Handles asynchronous communication between ERP modules (Finance, HR, SCM, Manufacturing, CRM)
import asyncio
Ensures reliable delivery, persistence, and dead-letter handling for critical business events.
"""
import aio_pika
from aio_pika import Message, ExchangeType, DeliveryMode
from typing import Any, Dict, Optional
import json
import logging
from backend.app.core.config import settings

logger = logging.getLogger(__name__)

class EnterpriseEventBus:
    def __init__(self):
        self.connection: Optional[aio_pika.Connection] = None
        self.channel: Optional[aio_pika.Channel] = None
        self.exchanges: Dict[str, aio_pika.Exchange] = {}
        self._reconnect_delay = 5

    async def connect(self):
        """Establish connection to RabbitMQ with retry logic"""
        while True:
            try:
                self.connection = await aio_pika.connect_robust(
                    settings.RABBITMQ_URL,
                    client_properties={"connection_name": "erp_core_service"}
                )
                self.channel = await self.connection.channel()
                await self.channel.set_qos(prefetch_count=100)
                
                # Declare core domain exchanges
                domains = ["finance", "hrm", "scm", "manufacturing", "crm"]
                for domain in domains:
                    exchange = await self.channel.declare_exchange(
                        f"erp.{domain}",
                        ExchangeType.TOPIC,
                        durable=True
                    )
                    self.exchanges[domain] = exchange
                
                logger.info("Enterprise Event Bus connected successfully")
                return
            except Exception as e:
                logger.error(f"RabbitMQ connection failed: {e}. Retrying in {self._reconnect_delay}s...")
                await asyncio.sleep(self._reconnect_delay)

    async def publish_event(self, domain: str, routing_key: str, payload: Dict[str, Any], mandatory: bool = True):
        """
        Publish event to specific domain exchange.
        Used for: Journal Posting, Order Fulfillment, Payroll Processing, Inventory Updates
        """
        if domain not in self.exchanges:
            raise ValueError(f"Unknown domain: {domain}")
        
        message = Message(
            body=json.dumps(payload).encode(),
            delivery_mode=DeliveryMode.PERSISTENT,
            content_type="application/json",
            headers={"erp_version": "2.0", "source": "core_service"}
        )
        
        try:
            await self.exchanges[domain].publish(message, routing_key=routing_key, mandatory=mandatory)
            logger.debug(f"Event published: {domain}.{routing_key}")
        except Exception as e:
            logger.error(f"Failed to publish event {routing_key}: {e}")
            raise

    async def subscribe(self, domain: str, queue_name: str, callback, routing_key: str = "#"):
        """
        Subscribe to domain events.
        Creates durable queue with Dead Letter Exchange (DLX) support.
        """
        if domain not in self.exchanges:
            raise ValueError(f"Unknown domain: {domain}")

        # Declare DLX
        dlx_exchange = await self.channel.declare_exchange(f"{queue_name}.dlx", ExchangeType.DIRECT, durable=True)
        dlx_queue = await self.channel.declare_queue(f"{queue_name}.dead_letter", durable=True)
        await dlx_queue.bind(dlx_exchange, routing_key="dead_letter")

        # Declare main queue with DLX argument
        queue = await self.channel.declare_queue(
            queue_name,
            durable=True,
            arguments={"x-dead-letter-exchange": f"{queue_name}.dlx"}
        )
        
        await queue.bind(self.exchanges[domain], routing_key=routing_key)
        
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    try:
                        payload = json.loads(message.body.decode())
                        await callback(payload)
                    except Exception as e:
                        logger.error(f"Error processing message in {queue_name}: {e}")
                        # Message automatically requeued or sent to DLX based on ack/nack

    async def close(self):
        if self.connection:
            await self.connection.close()

# Global instance
event_bus = EnterpriseEventBus()
