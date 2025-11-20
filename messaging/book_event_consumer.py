import aio_pika
import json
from loadModels import refresh_cache
from messaging.rabbitmq_config import RABBITMQ_URL

async def book_event_start_consumer():
    book_events = ["book.added", "book.updated", "book.deleted"]
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    channel = await connection.channel();
    
    queue = await channel.declare_queue("book.cache", durable=True)
    
    
    #define callback function that will process received messages
    async def callback(message: aio_pika.IncomingMessage):
        async with message.process():
            try:
                body = json.loads(message.body.decode())
                event = body.get('eventName')
                book_id = bosy.get('bookId')
            
                if event in book_events:
                    refresh_cache() 
                
            except Exception as e:
                print(f"Error handling received message: {e}")
    
    await queue.consume(callback)
        
            