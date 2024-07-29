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
python3 manage.py collectstatic --noinput
echo "Collect static files done"

# Check availability of static files
if [ ! -d "/app/staticfiles" ]; then
    echo "Static files not found"
    exit 1
fi

echo "Make migrations..."
python3 manage.py makemigrations
echo "Make migrations done"

echo "Apply database migrations..."
python3 manage.py migrate
echo "Apply database migrations done"

# Start the server using Daphne for ASGI
echo "Starting server..."

# Check if nginx service is running
if pgrep nginx > /dev/null
then
    echo "Nginx is running"
else
    echo "Nginx is not running, starting nginx..."
    service nginx start
fi

daphne core.asgi:application --port 8001 --bind 0.0.0.0 -v 3

# Execute any additional commands passed to the script
exec "$@"
