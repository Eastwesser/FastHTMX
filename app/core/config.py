# config.py — здесь можно хранить конфигурации, такие как настройки базы данных, секреты и другие важные параметры.
# app/core/config.py

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastHTMX Project"
    API_V1_STR: str = "/api/v1"
    CSRF_SECRET: str = "your-secret-key"


settings = Settings()
