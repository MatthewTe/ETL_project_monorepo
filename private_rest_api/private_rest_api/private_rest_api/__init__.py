# Importing Celery packages:
from .celery import app as celery_app

__all__ = ("celery_app")

# TODO: Address Secuirty issues with production deployment. 
# TODO: Add project description for git repo README. Add Github project and wiki.
# TODO: Create a scheduled database backup process.
# TODO: Look at creating a pipeline for CI/CD (webhooks, ansible playlists, etc).