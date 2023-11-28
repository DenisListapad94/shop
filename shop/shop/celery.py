import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery('shop')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every 1 minutes
    'summa': {
        'task': 'ecoshop.tasks.summa',
        'schedule': crontab(minute="*/1"),
        'args': (16, 16),
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()