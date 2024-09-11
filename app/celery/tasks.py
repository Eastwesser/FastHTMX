from app.celery.celery_app import celery_app


@celery_app.task
def example_task():
    return "Task completed"
