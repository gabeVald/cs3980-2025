from functools import lru_cache
import os
from dotenv import load_dotenv

from models.my_config import MyConfig

# Load the environment variables
load_dotenv()



@lru_cache
def get_settings():
    return MyConfig()

settings = get_settings()

print(settings.password)

print(settings.connection_string)

print(settings.max_user)

print(settings.max_salary)