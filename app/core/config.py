# config.py — здесь можно хранить конфигурации, такие как настройки базы данных, секреты и другие важные параметры.
# app/core/config.py
from pydantic import (
    BaseModel,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    # url: PostgresDsn
    url: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class CeleryConfig(BaseModel):
    broker_url: str = "amqp://guest:guest@localhost:5672//"  # RabbitMQ
    result_backend: str = "redis://localhost:6379/0"  # Redis
    task_serializer: str = "json"
    accept_content: list[str] = ["json"]
    timezone: str = "UTC"
    enable_utc: bool = True


class RedisConfig(BaseModel):
    url: str = "redis://localhost:6379/1"


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastHTMX Project"
    API_V1_STR: str = "/api/v1"
    CSRF_SECRET: str = "8148b7148634eeb37192a3d9ebcac7f877a8db21763f667ddaae3d065ba41ce0"
    DATABASE_URL: str = "postgresql+asyncpg://user:pwd@localhost:5432/app"
    REDIS_URL: str = "redis://localhost:6379/1"

    model_config = SettingsConfigDict(
        extra='allow',  # Оставить запрет дополнительных полей
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig(url="postgresql+asyncpg://user:pwd@localhost:5432/app")
    celery: CeleryConfig = CeleryConfig()
    redis: RedisConfig = RedisConfig()


settings = Settings()
