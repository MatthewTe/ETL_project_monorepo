# Native Django Imports:
from django.shortcuts import render
from django.http import JsonResponse

# DRF Imports:
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination

# Importing Twitter Models, Serializers, Filters and Paginators:
from .models import TrendingTwitterTopic
from .filters import TrendingTwitterTopicFilter
from .serializers import TrendingTwitterTopicSerializer
from .pagination import TrendingTwitterTopicPagination

# Importing schema documentation methods:
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

parameter_schema=[

            openapi.Parameter(
                "name",
                openapi.IN_QUERY,
                description="Filters the trending topics by the name of the topic. Only topics that contain this value will be returned.",
                type=openapi.TYPE_STRING,
                required=False
            ),

            openapi.Parameter(
                "location",
                openapi.IN_QUERY,
                description="Specifies the location for trending topics. The location field filters topics based on its conventonal name eg: 'Canada' or 'Waterloo'", 
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
schema_description="The endpoint that provides all the trending twitter topics for all available locations. There are various query parameters that can be used to refine the dataset. See our API documentation for more details."
@swagger_auto_schema(method="get", manual_parameters=parameter_schema, operation_description=schema_description)
@api_view(('GET',))
def trending_twitter_topics(request):
    """The API view that provdes trending twitter topics by processing incoming GET requests.

    It filters the queryset based on the url params that are provded by the incoming GET request.

    Arguments:
        
        name (str): The name of the trending topic.
        
        start-date (yyyy-mm-dd): Trending topics only on or after this date will be returned.
        
        end-date (yyyy-mm-dd): Trending topics up to (including) this date will be returned.

        location (str): Only trending topics from this local area will be returned. Trending
            topics are queried by the 'name' value of the twitter region. 

    """
    # Creating the main queryset:
    queryset = TrendingTwitterTopic.objects.all()

    # Creating and configuring pagination:
    paginator = TrendingTwitterTopicPagination()

    # Applying filters based on queryset params in GET request:
    filterset = TrendingTwitterTopicFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
        queryset = filterset.qs

    # Paginating the queryset:
    queryset = paginator.paginate_queryset(queryset, request)

    # Seralizing the data into a JSON response and returning the data:
    seralized_queryset = TrendingTwitterTopicSerializer(queryset, many=True, context={'request':request})

    return Response(seralized_queryset.data, status=status.HTTP_200_OK)