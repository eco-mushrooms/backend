#!/bin/sh

echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Collect static files done"

echo "Make migrations..."
python manage.py makemigrations
echo "Make migrations done"

echo "Apply database migrations..."
python manage.py migrate
echo "Apply database migrations done"

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000

exec "$@"