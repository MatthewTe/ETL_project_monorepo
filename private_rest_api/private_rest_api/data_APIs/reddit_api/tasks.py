from __future__ import absolute_import, unicode_literals 

# Importing celery packages:
from celery import shared_task

# Importing database models and extraction methods:
from .models import RedditDeveloperAccount, Subreddit, RedditPosts
from .data_extraction import extract_reddit_posts 
#from reddit_api.data_extraction import

@shared_task
def perform_reddit_ingestion():
    """The celery task that performs the data ingestion for all subreddit posts via
    the 'extract_reddit_posts' method. It performs scheduled data ingestion for both
    top and hot posts.
    
    """
    # Querying the subreddits and the Developer Account:
    dev_account = RedditDeveloperAccount.objects.first()
    subreddits = Subreddit.objects.all()

    # Performing data ingestion for 'top' and 'hot' posts:
    extract_reddit_posts(
        dev_client_id=dev_account.dev_client_id,
        dev_secret=dev_account.dev_secret,
        dev_user_agent=dev_account.dev_user_agent,
        subreddits=subreddits,
        post_filter="top"
    )

    extract_reddit_posts(
        dev_client_id=dev_account.dev_client_id,
        dev_secret=dev_account.dev_secret,
        dev_user_agent=dev_account.dev_user_agent,
        subreddits=subreddits,
        post_filter="hot"
    )