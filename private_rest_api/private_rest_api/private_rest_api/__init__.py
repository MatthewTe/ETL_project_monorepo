# Importing Celery packages:
from .celery import app as celery_app

__all__ = ("celery_app")

# TODO: Address Secuirty issues with production deployment. 
# TODO: Add project description for git repo.

# TODO: Make the core url "/" display a map of the DRF schema via OpenAPI Schema. 
# https://www.django-rest-framework.org/api-guide/schemas/
# https://www.django-rest-framework.org/topics/documenting-your-api/#self-describing-apis

# TODO: Create a markdown styled description of the reddit endpoint.
# TODO: Correctly Style the main Swagger Homepage. https://drf-yasg.readthedocs.io/en/stable/index.html

# TODO: Create a scheduled database backup process.