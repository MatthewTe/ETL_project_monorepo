#!/bin/sh
sleep 7

# Launching the Celery Beat Scheduler daemon:
if [ "$PRODUCTION" = True ]; then 

    echo "Running the Celery Beat Scheduler in the Production environment"
    celery -A private_rest_api beat -l INFO --schedule=django_celery_beat.schedulers:DatabaseScheduler
else

    echo "Running the Celery Beat Scheduler in the Development environment"
    celery -A private_rest_api beat -l INFO --schedule=django_celery_beat.schedulers:DatabaseScheduler
fi