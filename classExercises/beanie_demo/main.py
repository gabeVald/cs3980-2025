from functools import lru_cache
import os
from dotenv import load_dotenv

from models.my_config import MyConfig

# Load the environment variables
load_dotenv()



@lru_cache
def get_settings():
    return MyConfig()

setting = get_settings()

print(setting.password)

print(setting.connection_string)

print(setting.max_user)

print(setting.max_salary)