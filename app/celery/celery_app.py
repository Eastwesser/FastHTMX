from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.celery.broker_url,
    backend=settings.redis.url
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@celery_app.task
def example_task():
    return "Task completed!"
