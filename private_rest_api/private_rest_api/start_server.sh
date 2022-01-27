#!/bin/sh

# Collecting static files:
echo "Performing Static File Collection"
python manage.py collectstatic --noinput

# Applying Database Migrations:
echo "Making Database Migrations"
python manage.py makemigrations
python manage.py migrate 

# Starting the celery schedueler processes:
echo "Starting the celery worker and the celery-beat scheduler then the gunicorn server"
celery -A private_rest_api worker -l INFO &\\
celery -A private_rest_api beat -l INFO & \\
gunicorn private_rest_api.wsgi:application --bind 0.0.0.0:80
#python manage.py runserver 0.0.0.0:8000


