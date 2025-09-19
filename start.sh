#!/bin/bash

# Exit on any error
set -e

echo "Starting StudyHub deployment..."

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Set up initial data
echo "Setting up initial data..."
python manage.py setup_initial_data

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create a superuser if none exists
echo "Checking for superuser..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(is_superuser=True).exists():
    print('No superuser found. Creating one...')
    User.objects.create_superuser('admin', 'admin@studyhub.com', 'admin123')
    print('Superuser created: username=admin, password=admin123')
else:
    print('Superuser already exists')
"

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn studyhub.wsgi:application --log-file -
