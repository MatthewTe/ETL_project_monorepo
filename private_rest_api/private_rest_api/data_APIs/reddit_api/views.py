# Native Django Imports:
from django.shortcuts import render
from django.http import JsonResponse

# DRF Imports:
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Importing Reddit Models, Serializers, Filters and Paginators:
from .models import RedditPosts, RedditDeveloperAccount, Subreddit
from .serializers import RedditPostsSerializer, SubredditSerializer
from .filters import RedditPostFilter
from .pagination import RedditEndpointPagination

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
@permission_classes([IsAuthenticatedOrReadOnly])
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
                "title",
                openapi.IN_QUERY,
                description="Posts with a title that contains this value will be returned.",
                type=openapi.TYPE_STRING,
                required=False
            ),
            
            openapi.Parameter(
                "content",
                openapi.IN_QUERY,
                description="Posts that have content that contains this value will be returned.",
                type=openapi.TYPE_STRING,
                required=False
            ),

            openapi.Parameter(
                "subreddit",
                openapi.IN_QUERY,
                description="Only posts that come from this subreddit will be returned eg: politics",
                type=openapi.TYPE_STRING,
                required=False
            ),

            openapi.Parameter(
                "start_date",
                openapi.IN_QUERY,
                description="Only posts at or after the specified date will be returned. Must be in the format yyyy-mm-dd",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                "end_date",
                openapi.IN_QUERY,
                description="Only posts posted up to (excluding) this date will be returned. Must be in the format yyyy-mm-dd",
                type=openapi.TYPE_STRING,
                required=False
            ),

            openapi.Parameter(
                "per_page",
                openapi.IN_QUERY,
                description="This specifies the number of items that will be returned per query. This is set by default to 200 due to performance limitations of the Swagger UI. For use this can be set as large as you require.",
                type=openapi.TYPE_INTEGER,
                required=False,
                default=200
            )

        ] 
schema_description = "The endpoint that provides structured reddit post data for all the supported subreddits (which can be determined via the subreddit endpoint). There are various query parameters that can be used to refine the dataset. See our API documentation for more details. "
@swagger_auto_schema(method="get", manual_parameters=parameter_schema, operation_description=schema_description)
@api_view(["GET"])
def reddit_posts(request):
    """The API view that provides reddit posts data by processing incoming GET requests.
    
    It filters the queryset based on the url params that are provded by the incoming GET request.

    Arguments:
        
        title (str): The title of the reddit post can be filtered based on if it contains the string.

        content (str): The main body of the reddit post can be filtered based on if it contains the string. 

        subreddit (str): The dataset can be filtered based on the subreddit of the post. Eg: "politics"

        start-date (yyyy-mm-dd): Reddits Posts only on or after this date will be returned.
        
        end-date (yyyy-mm-dd): Reddits Posts up to (including) this date will be returned.
        
    """        
    # Creating the queryset to be filtered:
    queryset = RedditPosts.objects.all()

    # Creating and configuring pagination:
    paginator = RedditEndpointPagination()

    # Applying filters based on query parameters in GET request:
    filterset = RedditPostFilter(request.GET, queryset=queryset) 
    if filterset.is_valid():
        queryset = filterset.qs

    # Paginating the queryset:
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    
    # Seralizing the data into a JSON response and returning the data:
    seralized_queryset = RedditPostsSerializer(paginated_queryset, many=True, context={'request': request})
    
    return paginator.get_paginated_response(seralized_queryset.data)