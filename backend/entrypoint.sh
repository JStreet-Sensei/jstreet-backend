#!/bin/sh
# Wait for Postgres to be ready
/wait-for-postgres.sh postgresdb

# Perform database migration
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Seed data
python manage.py loaddata api/fixtures/users.json
python manage.py loaddata api/fixtures/initial_data.json

# Create default super user
python manage.py createsuperuser --noinput

# Start Django application with Gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:8000