from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = "sqlite:///./todo_app.db"
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Better Auth settings
    BETTER_AUTH_SECRET: str = "your-better-auth-secret"

    class Config:
        env_file = ".env"


settings = Settings()