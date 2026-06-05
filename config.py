from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    DB_HOST: str = ''
    DB_PORT: int = 0
    POSTGRES_DB: str = ''
    POSTGRES_USER: str = ''
    POSTGRES_PASSWORD: str = ''

    JWT_SECRET_KEY: str = ''
    AI_KEY: str = ''
    
    model_config = SettingsConfigDict(env_file='.env')

    @property
    def async_db_url(self) -> str:
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}'


@lru_cache
def get_settings():
    return Settings()

settings = get_settings()