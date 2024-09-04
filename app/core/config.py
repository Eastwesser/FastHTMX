# config.py — здесь можно хранить конфигурации, такие как настройки базы данных, секреты и другие важные параметры.
# app/core/config.py
from pydantic import BaseModel
from pydantic import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()

    PROJECT_NAME: str = "FastHTMX Project"
    API_V1_STR: str = "/api/v1"
    CSRF_SECRET: str = "8148b7148634eeb37192a3d9ebcac7f877a8db21763f667ddaae3d065ba41ce0"

    # db
    db_url: str


settings = Settings()
