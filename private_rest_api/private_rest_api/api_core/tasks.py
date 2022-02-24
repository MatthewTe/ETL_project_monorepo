from __future__ import absolute_import, unicode_literals 

# Importing celery packages:
from celery import shared_task

# Importing specific models from each app for inclusion in the email: 
from data_APIs.reddit_api.models import RedditPosts
from data_APIs.twitter_api.models import TrendingTwitterTopic

# Importing email methods:
from django.core.mail import send_mail


def send_status_update_email():
    """The celery task 
    """
    pass