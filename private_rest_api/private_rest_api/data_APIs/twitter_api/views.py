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

parameter_schema=[]
schema_description=""
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
    # TODO: Write Endpoint Logic.
    return Response({"test"}, status=status.HTTP_200_OK)