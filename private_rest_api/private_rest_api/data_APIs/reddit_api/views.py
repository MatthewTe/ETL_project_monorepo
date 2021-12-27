# Native Django Imports:
from django.shortcuts import render
from django.http import JsonResponse

# DRF Imports:
from rest_framework import viewsets

# Importing Reddit Models and Serializers:
from .models import RedditPosts
from .serializers import RedditPostsSerializer


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
        """The Ingestion method allowing seralized reddit post data to be
        written to the project's database. 
        """
        # Creating a context dict to be populated:
        context = {}
        context['request'] = request
        
        queryset = RedditPosts.objects.all().order_by("created_on")

        # If Requests Body contains POST data:
        if request.body:
            posts = json.loads(request.body)
        else:
            posts = {} # Empty Json if no body content.

        # Performing a bulk insert for all posts recieved by the POST request:
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
                "author_is_gold":post["author_gold"],
                "author_mod":post["mod_status"],
                "author_has_verified_email":post["verified_email_status"],
                "permalink":post["link"],
                "author":post["author"],
                "author_created":post["acc_created_on"],
                "comment_karma":post["comment_karma"]}                
            ) for post in posts
        ]
        
        # Seralizing the objects that had been creatd:
        posts_objects = [post[0] for post in posts_objects]
        serializer = RedditPostsSerializer(posts_objects, many=True, context=context)
        
        return Response(serializer.data)