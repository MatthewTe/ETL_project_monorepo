# Importing Celery packages:
from .celery import app as celery_app

__all__ = ("celery_app")

# TODO: In production I need to remove authentication for the home pages. Auth in production does not need to exist yet.

# TODO: Make the core url "/" display a map of the DRF schema via OpenAPI Schema. 
# https://www.django-rest-framework.org/api-guide/schemas/
# https://www.django-rest-framework.org/topics/documenting-your-api/#self-describing-apis

# TODO: Create a markdown styled description of the reddit endpoint.

# TODO: Create a scheduled database backup process.