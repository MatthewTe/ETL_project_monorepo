# Importing Celery packages:
from .celery import app as celery_app

__all__ = ("celery_app")

# TODO: Make the core url "/" display a map of the DRF schema via OpenAPI Schema. 
# https://www.django-rest-framework.org/api-guide/schemas/
# https://www.django-rest-framework.org/topics/documenting-your-api/#self-describing-apis
# TODO: Create a markdown styled description of the reddit endpoint.

# TODO: Add nginx server to monorepo to route external traffic to REST API.

# TODO: Create a way of dynamically generating settings for prod and dev environments