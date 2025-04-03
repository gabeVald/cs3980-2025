from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import certifi
import ssl

from main import get_settings
from models.product import Product


async def init_db():
    my_config = get_settings()
    # Create an SSL context with the certificates from certifi
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    # Use the SSL context in the MongoDB client
    client = AsyncIOMotorClient(my_config.connection_string, tlsCAFile=certifi.where())
    db = client['test_db']
    await init_beanie(database=db, document_models=[Product])
    
    # Create some sample products
    product1 = Product(name="Laptop", description="High-performance laptop")
    product2 = Product(name="Smartphone", description="Latest smartphone model")
    
    # Insert the products into the database
    #await product1.insert()
    #await product2.insert()
    
    # Find all products and print them
    all_products = await Product.find_all().to_list()
    print("Products in database:")
    for product in all_products:
        print(f"- {product.name}: ${product.description}")


asyncio.run(init_db())