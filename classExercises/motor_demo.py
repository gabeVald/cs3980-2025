from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def main():
    client = AsyncIOMotorClient("this is the address of the database when you've made it")

    """
    If you want this to work, the database name needs to be in the connection string: localhost:1923/DEFAULTDBNAME

    default_database = client.get_default_database()
    print(default_database)
    """
    databases = await client.list_database_names()
    print(databases)

asyncio.run(main())
