from __future__ import absolute_import, unicode_literals 

# Importing celery packages:
from celery import shared_task

# Importing database models and extraction methods:
from .models import TwitterRegion, TwitterDeveloperAccount, TrendingTwitterTopic
from .data_extraction import extract_trending_topics, extract_twitter_regions

@shared_task
def perform_twitter_location_ingestion():
    """The celery task that ingests the location data from the twitter API via the
    'extract_twitter_regions' method. 
    
    It relies on a TwitterDeveloperAccount being present in the database.

    """
    # Querying developer credentials:
    dev_account = TwitterDeveloperAccount.objects.first()
    
    # Initalizing the extraction method w/ the dev credientials:
    extract_twitter_regions(
        api_key=dev_account.api_key,
        api_secret_key=dev_account.api_secret_key,
        access_token=dev_account.access_token,
        access_token_secret=dev_account.access_token_secret
    )

@shared_task
def perform_twitter_trending_ingestion():
    """The celery task that ingests the trending twitter topic data via the Twitter API 
    and the 'extract_trending_topics' method.

    It relies on a TwitterDeveloperAccount being present in the database and twitter API 
    locations via the TwitterRegion object. Typically this means that the 'perform_twitter_location_ingestion'
    task needs to have executed at least once for this task to execute successfully.

    """
    # Querying developer credentials and location:
    dev_account = TwitterDeveloperAccount.objects.first()
    locations = TwitterRegion.objects.all()

    # Initalizing the extracting method:
    extract_trending_topics(
        api_key=dev_account.api_key,
        api_secret_key=dev_account.api_secret_key,
        access_token=dev_account.access_token,
        access_token_secret=dev_account.access_token_secret,
        locations=locations
    )
