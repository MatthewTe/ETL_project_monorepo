# Importing Reddit API:
import praw

# Importing datetime manipulation packages:
import time
from datetime import date, timedelta, datetime
import pytz

# Importing Requests packages:
import json
import requests

# Importing Reddit Database Models:
from .models import RedditPosts, Subreddit

# Function that extracts reddit posts and POSTs said data to a REST API (aggregates all other methods):
def extract_reddit_posts(**kwargs):
    """The main method that when initialized uses the Reddit API praw to query the top and best posts
    from each subreddit provided in the kwargs. These posts are then written to the database via the 
    creation of RedditPosts models.

    Args:
        dev_client_id (str): The reddit developer account id.
        
        dev_secret (str): The secret key for the reddit developer account.

        dev_user_agent (str): The user agent (application description string) of the reddit developer account.

        subreddits (lst [Subreddit]): A list of subreddit objects that will be used to determine what subreddits
            are queried to get posts. It is a list of subreddit database models that are also used to create the   
            foregin key connection between the Subreddit model and the RedditPosts model.

        post_filter (str): The str determining if the 'top' or 'best' reddit posts will be extracted from the
            subreddit.

    """
    # Unpacking kwargs:
    dev_app_id = kwargs.get("dev_client_id")
    dev_app_secret = kwargs.get("dev_secret")
    dev_app_usr_agent = kwargs.get("dev_user_agent")

    # Config for what reddit posts to extract:
    subreddits = kwargs.get("subreddits")
    reddit_filter = kwargs.get("post_filter", "top")

    # Creating a reddit praw object:
    reddit = praw.Reddit(
        client_id = dev_app_id,
        client_secret = dev_app_secret,
        user_agent = dev_app_usr_agent
    )
    reddit.read_only = True

    # Performing data extraction and ingestion for each subreddit:
    for subreddit in subreddits:
        subreddit_instance = reddit.subreddit(subreddit.name)
        
        # Determining which filter to apply to the subreddit post extraction and serializing posts:
        if reddit_filter == "top":
            posts = [post_serializer(post, subreddit) for post in subreddit_instance.top("day", limit=25)]
           
        elif reddit_filter == "hot":
            posts = [post_serializer(post, subreddit) for post in subreddit_instance.hot(limit=25)]
    
        # Creating database models: and writing data to the database:
        posts_objects = [
            RedditPosts.objects.update_or_create(
                id = post["id"],
                defaults= {
                "id":post["id"],
                "subreddit": post["subreddit"],
                "title":post["title"],
                "content":post["content"],
                "upvote_ratio":post["upvote_ratio"],
                "score":post["score"],
                "num_comments":post["num_comments"],
                "created_on":post["created_on"],
                "stickied":post["stickied"],
                "over_18":post["over_18"],
                "spoiler":post["spoiler"],
                "author_is_gold":post["author_is_gold"],
                "author_mod":post["author_mod"],
                "author_has_verified_email":post["author_has_verified_email"],
                "permalink":post["permalink"],
                "author":post["author"],
                "author_created":post["author_created"],
                "comment_karma":post["comment_karma"]}                
            ) for post in posts
        ] 

def post_serializer(post, subreddit):
    """Function that takes in a praw post object extracted from reddit and
    serializes it into a format that is compatable with the private REST API
    that the ingestion is designed for.

    Args: 
        post (praw.Reddit.post): The praw reddit post object from which all the data 
            will be extracted.

        subreddit (db.Models): The subreddit instance used to create a ForeginKey field.

    Return:
        dict: The dict containing the seralized data from the praw post object.

    """
    # Reddit Post Dict to be populated:
    reddit_post = {}

    # Extracting the "problamatic" elements from the post object:
    try:
        reddit_post["author_is_gold"] = post.author.is_gold
    except:
        reddit_post["author_is_gold"] = None
    try:
        reddit_post["author_mod"] = post.author.is_mod
    except:
        reddit_post["author_mod"] = None
    try:
        reddit_post["author_has_verified_email"] = post.author.has_verified_email
    except:
        reddit_post["author_has_verified_email"] = None
    try:
        reddit_post["comment_karma"] = post.author.comment_karma
    except:
        reddit_post["comment_karma"] = None 
    try:
        reddit_post["author_created"] = _format_datetime(post.author.created_utc)
    except:
        reddit_post["author_created"] = None

    # Extracting the basic elements from the post object:
    reddit_post = {
        **reddit_post,
        "id":post.id,
        "subreddit":subreddit, 
        "title": post.title,
        "content": post.selftext,
        "upvote_ratio": post.upvote_ratio,
        "score": post.score,
        "num_comments": post.num_comments,
        "stickied": post.stickied,
        "over_18": post.over_18,
        "spoiler": post.spoiler,
        "permalink": post.permalink,
        "author": post.author,
        "created_on": _format_datetime(post.created_utc)
    }    
    time.sleep(0.5)
    return reddit_post

def _format_datetime(utc_float):
    """Method ingests a utc timestamp float and formats it into
    a datetime format that is prefered by the DRF framework.
    It performs conversions through datetime and pytz.
    Args:
        utc (float): A unix timestamp.   
        
    Returns:
        str: The formatted datetime in string format.
    """
    date_obj = datetime.fromtimestamp(utc_float, tz=pytz.utc)
    date_str = date_obj.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    return date_str
