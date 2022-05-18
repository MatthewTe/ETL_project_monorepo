from __future__ import absolute_import, unicode_literals

# Native Package imports:
import os

# Importing Celery methods:
from celery import Celery

# Django Settings modules:
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "private_rest_api.settings")

# Creating and Configuring Celery app:
app = Celery("private_rest_api")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()    