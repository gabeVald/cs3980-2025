from beanie import init_beanie

from models.my_config import get_settings
from models.todo import Todo
from models.user import User

from motor.motor_asyncio import AsyncIOMotorClient
import certifi
import ssl


async def init_database():
    my_config = get_settings()
    # Create an SSL context with the certificates from certifi
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    # Use the SSL context in the MongoDB client
    client = AsyncIOMotorClient(my_config.connection_string, tlsCAFile=certifi.where())
    db = client['todo_app']
    await init_beanie(database=db, document_models=[User, Todo])
