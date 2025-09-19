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
from core.models import UserProfile

if not User.objects.filter(is_superuser=True).exists():
    print('No superuser found. Creating one...')
    User.objects.create_superuser('admin', 'admin@studyhub.com', 'admin123')
    print('Superuser created: username=admin, password=admin123')
else:
    print('Superuser already exists')

# Ensure all users have profiles
print('Checking user profiles...')
users_without_profiles = User.objects.filter(profile__isnull=True)
if users_without_profiles.exists():
    print(f'Found {users_without_profiles.count()} users without profiles. Creating...')
    for user in users_without_profiles:
        UserProfile.objects.create(user=user, education_level=UserProfile.BACHELORS)
    print('All user profiles created')
else:
    print('All users have profiles')
"

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn studyhub.wsgi:application --log-file -
