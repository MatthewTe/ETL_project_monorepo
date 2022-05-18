#!/bin/sh
sleep 12

# Running the flower daemon based on if the environment is development or production:
if [ "$PRODUCTION" = True ]; then

    echo "Running Flower in a Production environment"
    # Running with the Github Auth system:
    celery flower --auth_provider=$FLOWER_AUTH_SCHEME --auth=$FLOWER_GIT_EMAIL
else

    echo "Running Flower in a Development environment"
    # Running without the auth system:
    celery flower
fi