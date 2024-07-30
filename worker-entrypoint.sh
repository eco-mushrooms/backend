#! /bin/sh

echo "Starting celery worker..."

celery -A core worker --loglevel=info --concurrency=1 -E

