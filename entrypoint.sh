#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

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
daphne core.asgi:application --port 8000 --bind 0.0.0.0 -v 3

exec "$@"