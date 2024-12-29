from pydantic_settings import BaseSettings
from pydantic import Field, model_validator
from typing import Optional

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: Optional[str] = Field(None)

    @model_validator(mode='after')
    def get_database_url(cls, values):
        values.DATABASE_URL = f'postgresql+asyncpg://{values.DB_USER}:{values.DB_PASS}@{values.DB_HOST}:{values.DB_PORT}/{values.DB_NAME}' # Изменено обращение к атрибутам
        return values

    class Config:
        env_file = ".env"

settings = Settings()
print(settings.DATABASE_URL)

