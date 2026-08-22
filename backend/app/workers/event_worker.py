"""
Event Worker - Consumes events from RabbitMQ and processes them
Runs as a standalone worker service for asynchronous event handling
"""
import asyncio
import json
import signal
import logging
from typing import Dict, Any
from aio_pika import Message, IncomingMessage
import aio_pika
from app.config import settings
from app.websocket.event_bridge import event_bridge

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EventWorker:
    """Standalone worker for consuming and processing events from RabbitMQ"""
    
    def __init__(self):
        self.connection = None
        self.channel = None
        self.exchange = None
        self.queue = None
        self.running = True
        
    async def connect(self):
        """Establish connection to RabbitMQ"""
        logger.info(f"Connecting to RabbitMQ at {settings.RABBITMQ_URL}")
        try:
            self.connection = await aio_pika.connect_robust(str(settings.RABBITMQ_URL))
            self.channel = await self.connection.channel()
            
            # Declare exchange
            self.exchange = await self.channel.declare_exchange(
                settings.RABBITMQ_EXCHANGE, 
                aio_pika.ExchangeType.TOPIC,
                durable=True
            )
            
            # Declare queue for event consumption
            self.queue = await self.channel.declare_queue(
                "erp.events.worker",
                durable=True,
                auto_delete=False
            )
            
            # Bind queue to exchange with routing pattern
            await self.queue.bind(self.exchange, routing_key="erp.#")
            
            logger.info("Successfully connected to RabbitMQ")
        except Exception as e:
            logger.error(f"Failed to connect to RabbitMQ: {e}")
            raise
    
    async def process_message(self, message: IncomingMessage):
        """Process incoming message from queue"""
        async with message.process():
            try:
                body = json.loads(message.body.decode())
                event_type = body.get("event_type", message.routing_key or "unknown")
                
                logger.info(f"Processing event: {event_type}")
                
                # Forward to event bridge for WebSocket distribution
                await event_bridge.handle_event(event_type, body)
                
                logger.debug(f"Successfully processed event: {event_type}")
                
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON in message: {e}")
            except Exception as e:
                logger.error(f"Error processing message: {e}")
                # In production, send to dead-letter queue
    
    async def start_consuming(self):
        """Start consuming messages from queue"""
        if not self.queue:
            raise RuntimeError("Queue not initialized. Call connect() first.")
        
        logger.info("Starting event consumption...")
        await self.queue.consume(self.process_message)
        logger.info("Worker is now consuming events")
        
        # Keep running until stopped
        while self.running:
            await asyncio.sleep(1)
    
    async def stop(self):
        """Gracefully stop the worker"""
        logger.info("Stopping event worker...")
        self.running = False
        
        if self.connection and not self.connection.is_closed:
            await self.connection.close()
        
        logger.info("Event worker stopped")


async def main():
    """Main entry point for the worker"""
    worker = EventWorker()
    
    # Setup signal handlers for graceful shutdown
    loop = asyncio.get_event_loop()
    
    def signal_handler():
        logger.info("Received shutdown signal")
        asyncio.create_task(worker.stop())
    
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, signal_handler)
    
    try:
        await worker.connect()
        await worker.start_consuming()
    except KeyboardInterrupt:
        logger.info("Worker interrupted by user")
    except Exception as e:
        logger.error(f"Worker error: {e}")
        raise
    finally:
        await worker.stop()


if __name__ == "__main__":
    asyncio.run(main())
