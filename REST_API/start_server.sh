#!/bin/sh

# Displaying status information for the server/environment:
printf "
\nLaunching the REST API.
\nThe production status is: %s \nThe django settings file being used is: %s
\n\n" $PRODUCTION $DJANGO_SETTINGS_MODULE

if [ "$PRODUCTION" = True ]; then

    printf "\nRunning the Django Web Server in the Production Environment:\n"
    echo "Performing Static File Collection"
    python manage.py collectstatic --noinput
else

    printf "\nRunning the Django Web Server in the Development Environment:"
fi

# Applying Database Migrations:
echo "Making Database Migrations"
python manage.py makemigrations
python manage.py migrate 

# Starting the celery schedueler processes:
echo "Starting the gunicorn server"
gunicorn REST_API.wsgi:application --bind 0.0.0.0:$PORT --timeout 60