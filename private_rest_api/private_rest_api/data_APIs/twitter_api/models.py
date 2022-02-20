from django.db import models

class TwitterDeveloperAccount(models.Model):
    """The database model for Twitter Developer Accounts.

    It is designed to store all of the developer API keys for the Twitter Developer
    API account that the twitter python api makes use of to extract twitter data.

    https://developer.twitter.com/en/portal/dashboard

    """
    app_name = models.CharField(max_length=20)
    api_key = models.CharField(unique=True, max_length=25)
    api_secret_key = models.CharField(unique=True, max_length=50)
    bearer_token = models.CharField(unique=True, max_length=120)
    access_token = models.CharField(unique=True, max_length=50)
    access_token_secret = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.app_name

class TwitterRegion(models.Model):
    """All twitter regions that the twitter API has access to, centerd aroud Yahoo WOEIDs.

    Twitter uses a depreciated GeoID system called WOEID to break up regions in terms of trending
    topics. This model stores all WOEID regions that the twitter API provides and is populated via
    the '.available_trends()' method of the tweepy API.

    An avalible trend extracted from the API is as follows:

    {
        'name': 'Ottawa', 'placeType': {'code': 7, 'name': 'Town'}, 'url': 'http://where.yahooapis.com/v1/place/3369', 
        'parentid': 23424775, 'country': 'Canada', 'woeid': 3369, 'countryCode': 'CA'
    }  

    Only the relecant fields are extracted. 

    Attributes:

        name (models.CharField): The conventional name of the location.

        location_type (models.CharField): The type of location. Eg: Whether it is a "Country" or "Town".

        parentid (models.IntegerField): The WOEID of its parent Country. In the example, its parentid is the WOEID of
            Canada. If the locaiton is a country the WOEID is 1.
        
        country (models.CharField): The country the location is a part of. If the location is a country then this is same
            value as the 'name' field.

        woeid (models.IntegerField): The WOEID for the location.

        country_code (models.CharField): The country code for the location. 

    """
    name = models.CharField(max_length=100)
    location_type = models.CharField(max_length=20)
    parentid = models.IntegerField()
    country = models.CharField(max_length=100)
    woeid = models.IntegerField(unique=True)
    country_code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class TrendingTwitterTopic(models.Model):
    """The database model for a trending twitter topics.

    The twiiter python API allows us to pull trending twitter topics for each available
    region for a point in time. This data model stores trending topics for a region at a 
    point in time.

    The tweepy API pulls trending data in the form of a nested dictionary which, when unpacked
    is structed as follows: 

    {
        'name': 'Chelsea', 'url': 'http://twitter.com/search?q=Chelsea', 
        'promoted_content': None, 'query': 'Chelsea', 'tweet_volume': 798388
    } 

    with location and timestamp data being located in other areas of the data structure. The
    data model stores each instance of this trending data with timestamp data and location data
    that connects to the TwitterRegion model via a foregin key connection. 

    Attributes:

        name (models.CharField): The name of the trending topic. In the example it is 'Chelsea'.

        url (models.URLField): The url for the trending topic. 

        promoted_content (models.BooleanField): Field indicating if the trending topic is promoted content
            or not.

        topic_query (models.CharField): What the search query a user would have to enter in order to reach the topic.

        tweet_volume (models.IntegerField): The number of tweets associated with the topic at the time of extraciton.

        created_at (models.DateTimeField): The datetime that the topic was extracted by the pipeline.

        location (models.ForeignKey): The location for where the trending topic was found. It connects to the 
            TwitterRegion model via the WOEID field.          

    """
    name = models.CharField(max_length=100)
    url = models.URLField()
    promoted_content = models.BooleanField(null=True, blank=True)
    topic_query = models.CharField(max_length=100)
    tweet_volume = models.IntegerField(null=True)
    created_at = models.DateTimeField()
    location = models.ForeignKey(TwitterRegion, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}-{self.created_at}-{self.location}"