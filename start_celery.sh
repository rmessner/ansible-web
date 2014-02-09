export PYTHONUNBUFFERED=1

celery -A webapp:celery worker -l INFO
