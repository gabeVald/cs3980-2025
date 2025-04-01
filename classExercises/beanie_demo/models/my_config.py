from pydantic_settings import BaseSettings, SettingsConfigDict

class MyConfig(BaseSettings):
    password: str
    connection_string : str
    max_user: int
    #If we want a default value: max_user 2 not specified in .env
    max_user2: int= 1000
    max_salary: float


    model_config = SettingsConfigDict(env_file=".env")
