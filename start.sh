#!/bin/bash

# Exit on any error
set -e

echo "Starting StudyHub deployment..."

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn studyhub.wsgi:application --log-file -
