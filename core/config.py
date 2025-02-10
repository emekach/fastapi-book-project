import secrets

from pydantic_settings import BaseSettings
from dotenv import load_dotenv



class Settings(BaseSettings):
    PROJECT_NAME: str = "hng12-stage2"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "HNG12 DEVOPS x BACKEND (Stage 2)"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False

    RENDER_SERVICE_ID: str  # Will be loaded from .env
    RENDER_API_KEY: str  # Will be loaded from .env

    class Config:
        env_file = ".env"


settings = Settings()
