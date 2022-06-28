#!/bin/sh
sleep 5

# Launching the Celery Worker pool daemon:
if [ "$PRODUCTION" = True ]; then
    
    echo "Running the Worker Pool Daemon in the Production Environment"
    celery -A private_rest_api worker --loglevel=INFO --hostname=worker@%h --max-tasks-per-child=1 --max-memory-per-child 22000
else
    
    echo "Running the Worker Pool Daemon in the Development Environment"
    celery -A private_rest_api worker --loglevel=INFO --hostname=worker@%h
fi