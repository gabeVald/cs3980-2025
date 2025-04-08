from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import certifi

async def main():
    # Use certifi for SSL certificate verification
    client = AsyncIOMotorClient(
        "mongodb+srv://admin:<guUKMpwHIVaSQg8K>@mongodbassignment.vs3p442.mongodb.net/?retryWrites=true&w=majority&appName=mongoDBAssignment",
        tlsCAFile=certifi.where()
    )

    try:
        # List all databases
        databases = await client.list_database_names()
        print("Connected successfully!")
        print("Available databases:", databases)

    except Exception as e:
        print("An error occurred:", str(e))
    
    finally:
        # Close the connection
        client.close()

if __name__ == "__main__":
    asyncio.run(main())
