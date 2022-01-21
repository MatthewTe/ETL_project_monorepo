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
from .serializers import RedditPostsSerializer

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
        queryset = queryset.filter(subreddit=subreddit)
    
    queryset = queryset_datetime_filter(queryset, start_date, end_date) # by start and end date

    # Seralizing the data into a JSON response and returning the data:
    seralized_queryset = RedditPostsSerializer(queryset, many=True, context={'request': request})
    #json = JSONRenderer().render(seralized_queryset.data)

    return Response(seralized_queryset.data)