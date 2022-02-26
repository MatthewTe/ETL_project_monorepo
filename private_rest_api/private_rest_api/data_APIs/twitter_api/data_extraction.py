# Importing twitter API:
import tweepy 

# Importing datetime manipulation packages:
import time

# Importing models:
from .models import TwitterDeveloperAccount, TwitterRegion, TrendingTwitterTopic

# Function that gets all the avalible regions of the API and writing regions to the database:
def extract_twitter_regions(**kwargs):
    """The extraction method that uses the Twitter API to extract all the
    regions that are avalible fro the API to pull data from. 

    This method executes the tweepy api.available_trends() method to extract a list of
    available locations for the twitter API to pull data. This location data is then written
    into the database via the TwitterRegion model. It requires uses of the Twitter API and as 
    such requires an api account. This method was designed to be called as a scheduled task via
    the celery task scheduler.

    Args:
        api_key (str): API key for the twitter dev API.

        api_secret_key (str): Secret key for the twitter dev API.
        
        access_token (str): Access Token for the twitter dev API.
       
        access_token_secret (str): Access token Secret for the twitter dev API.
    
    """
    # Getting credientails to authenticate the API:
    # Unpacking Kwargs:
    API_KEY = kwargs.get("api_key")
    API_SECRET_KEY = kwargs.get("api_secret_key")
    ACCESS_TOKEN = kwargs.get("access_token")
    ACCESS_TOKEN_SECRET = kwargs.get("access_token_secret")

    # Autenticating and creating API:
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Querying all avalible locations:
    locations = api.available_trends()

    # Creating location database objects based on WOEID:
    location_objs = [
        TwitterRegion.objects.update_or_create(
            woeid=location["woeid"],
            defaults = {
                "woeid": location["woeid"],
                "name": location["name"],
                "location_type": location["placeType"]["name"],
                "parentid": location["parentid"],
                "country": location["country"], 
                "country_code": location["countryCode"]
            }
        ) for location in locations
    ]

# Function that queries and ingests trending topics for each avalible region from the API:
def extract_trending_topics(**kwargs):
    """The extraction function that ingests all of the trending twitter topics at that point in time.

    The method makes used of the tweepy api.get_place_trends() method to extract all the trending topics 
    for all of the locations specified and ingests trending data via the TrendingTwitterTopic model. It 
    requires uses of the Twitter API and as such requires an api account. This method was designed to be
    called as a scheduled task via the celery task scheduler. 

    Args:
        api_key (str): API key for the twitter dev API.

        api_secret_key (str): Secret key for the twitter dev API.
        
        access_token (str): Access Token for the twitter dev API.
       
        access_token_secret (str): Access token Secret for the twitter dev API.

        locations (QuerySet): A list of TwitterRegion objects dictating where to pull data from.

    """
    # Unpacking kwargs:
    API_KEY = kwargs.get("api_key")
    API_SECRET_KEY = kwargs.get("api_secret_key")
    ACCESS_TOKEN = kwargs.get("access_token")
    ACCESS_TOKEN_SECRET = kwargs.get("access_token_secret")
    locations = kwargs.get("locations")
    
    # Autenticating and creating API:
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Performing data extraction and ingestion:
    for location in locations:
        # Querying trending topics"
        topics = api.get_place_trends(location.woeid)

        # Extracting variables:
        created_at = topics[0]["created_at"]
        woeid = topics[0]["locations"][0]["woeid"]

        topic_objs = [
            TrendingTwitterTopic(
                name = topic["name"],
                url = topic["url"],
                promoted_content = topic["promoted_content"],
                topic_query = topic["query"],
                tweet_volume = topic["tweet_volume"],
                created_at = created_at,
                location = location

            ) for topic in topics[0]["trends"]
        ]

        # Sleeping to avoid breaking twitter API rate limit:
        time.sleep(1)

        # Bulk creating the db objects from the list:
        TrendingTwitterTopic.objects.bulk_create(topic_objs)


