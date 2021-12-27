#!/bin/sh

# Collecting static files:
echo "Performing Static File Collection"
python manage.py collectstatic --noinput

# Applying Database Migrations:
echo "Making Database Migrations"
python manage.py makemigrations
python manage.py migrate 

# Starting Server:
echo "Running Server"
gunicorn velkozz_web_api.wsgi:application --bind 0.0.0.0:8000

#python manage.py runserver 0.0.0.0:8000