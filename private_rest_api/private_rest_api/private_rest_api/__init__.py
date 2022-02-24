# Importing Celery packages:
from .celery import app as celery_app

__all__ = ("celery_app")

"NGINX"
# TODO: Add Cert-bot to for HTTPS: https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

"General Project"
# TODO: Address Secuirty issues with production deployment. 
# TODO: Incorporate Senty Logging/Error Management on Production Development.
# TODO: Create a scheduled database backup process.
# TODO: Look at creating a pipeline for CI/CD (webhooks, ansible playlists, etc).
# TODO: Create a scheduled email process that emails a daily status report on the server.  

"Twitter Application"
# TODO: Add API endpoint that serves trending data upon GET.
# TODO: Look at the code necessary to track tweets of specific figures.