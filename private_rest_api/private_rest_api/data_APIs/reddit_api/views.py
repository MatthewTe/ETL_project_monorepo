# Native Django Imports:
from django.shortcuts import render
from django.http import JsonResponse

# DRF Imports:
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# Importing Reddit Models and Serializers:
from .models import RedditPosts, RedditDeveloperAccount, Subreddit
from .serializers import RedditPostsSerializer, SubredditSerializer

# Importing schema documentation methods:
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Convience Methods:
def queryset_datetime_filter(queryset, start_date, end_date):
    """A method that appies start-date and end-date filtering to a
    database queryset.
    
    It assumes that the model field value that is being filtered via queryset is
    called 'created_on'. This method exists via convience to avoid repetition in
    filtering querysets.

    If the models in the queryset do not have a DateTime field called 'created_on'
    then this filtering will not work.

    Args:
        queryset (models.QuerySet): The django queryset that will be filtered using the 
            start and end date values.

        start_date (str|None): The start date to filter the queryset.

        end_date (str|None): The end date to filter the queryset.

    Returns:
        models.QuerySet: The queryset that has been filtered via start and end date.
    
    """
    # Applying the date time filtering:    
    if start_date is None and end_date is None:
        pass
    else:
        if end_date is None:
            queryset = queryset.filter(created_on__gt=start_date)

        if start_date is None:
            queryset = queryset.filter(created_on__lt=end_date)         

        if start_date and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date,end_date))
    
    return queryset

# Describing the Schema parameters for the api view:
schema_description="The endpoint that provides a list of all supported subreddits for the reddit posts endpoint."
@swagger_auto_schema(method="get", operation_description=schema_description)
@api_view(["GET"])
def subreddits(request):
    """The basic API endpoint that generates a list of subreddits when queried.
    """
    # Querying all subreddits:
    queryset = Subreddit.objects.all()

    # Seralizing the data into a JSON response and returning the data:
    seralized_queryset = SubredditSerializer(queryset, many=True, context={'request': request})

    return Response(seralized_queryset.data)

# Describing the Schema parameters for the api view:
parameter_schema = [
            openapi.Parameter(
                "Subreddit",
                openapi.IN_QUERY,
                description="Only posts that come from this subreddit will be returned eg: politics",
                type=openapi.TYPE_STRING,
                required=False
            ),

            openapi.Parameter(
                "Start-Date",
                openapi.IN_QUERY,
                description="Only posts at or after the specified date will be returned.",
                type=openapi.TYPE_STRING,
                pattern="yyyy-mm-dd",
                required=False
            ),
            openapi.Parameter(
                "End-Date",
                openapi.IN_QUERY,
                description="Only posts posted up to (excluding) this date will be returned. Must be in the format yyyy-mm-dd",
                type=openapi.TYPE_STRING,
                pattern="yyyy-mm-dd",
                required=False
            )
        ] 
schema_description = "The endpoint that provides structured reddit post data for all the supported subreddits (which can be determined via the subreddit endpoint). There are various query parameters that can be used to refine the dataset. See our API documentation for more details. "
@swagger_auto_schema(method="get", manual_parameters=parameter_schema, operation_description=schema_description)
@api_view(["GET"])
def reddit_posts(request):
    """The API view that provides reddit posts data by processing incoming GET requests.
    
    It filters the queryset based on the url params that are provded by the incoming GET request.

    Arguments:
        
        Subreddit (str): The dataset can be filtered based on the subreddit of the post. Eg: "politics"

        Start-Date (yyyy-mm-dd): Reddits Posts only on or after this date will be returned.
        
        End-Date (yyyy-mm-dd): Reddits Posts up to (including) this date will be returned.
        
    """
    # Extracting query params from url:
    subreddit = request.GET.get("Subreddit", None)
    start_date = request.GET.get("Start-Date", None)
    end_date = request.GET.get("End-Date", None)
        
    # Creating the queryset to be filtered:
    queryset = RedditPosts.objects.all()

    # Filtering the QuertSet:
    if subreddit is not None:
        queryset = queryset.filter(subreddit__name=subreddit)

    queryset = queryset_datetime_filter(queryset, start_date, end_date) # by start and end date

    # Seralizing the data into a JSON response and returning the data:
    seralized_queryset = RedditPostsSerializer(queryset, many=True, context={'request': request})
    #json = JSONRenderer().render(seralized_queryset.data)

    return Response(seralized_queryset.data) 