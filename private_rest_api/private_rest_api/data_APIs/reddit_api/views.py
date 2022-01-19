# Native Django Imports:
from django.shortcuts import render
from django.http import JsonResponse

# DRF Imports:
from rest_framework import viewsets

# Importing Reddit Models and Serializers:
from .models import RedditPosts, RedditDeveloperAccount, Subreddit
from .serializers import RedditPostsSerializer
from .data_extraction import extract_reddit_posts

class RedditPostViewSet(viewsets.ModelViewSet):
    """The ViewSet for the Reddit Posts Data model. The ViewSet
    provides all of the CRUD operations for the RedditPosts model and
    connects this model to the REST API. 
    """
    serializer_class = RedditPostsSerializer
    queryset = RedditPosts.objects.all().order_by("created_on")

    def list(self, request):
        """Dummy method to prevent GET requests to the API. This API only supports
        writing data.
        """
        return JsonResponse({"Error": "GET Requests to Database Not Supported on Private API. This API Supports Ingestion Only."})

    def create(self, request):
        """Dummy method to prevent POST requests to the API. This API only supports writing data. 

        """        
        return JsonResponse({"Error": "POST Requests to Database Not Supported on Private API."})