# Importing Django url modules:
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

#router = routers.DefaultRouter()

# Importing Reddit API Viewsets:
from .views import reddit_posts, subreddits

# Adding reddit REST API routes to the router:
#router.register(r"posts", RedditPostsAPI, basename="RedditPosts")

# Creating Automatic URL Routing:
urlpatterns = [
    path(r"subreddits/", subreddits, name="Subreddits"),
    path(r"posts/", reddit_posts, name="Reddit Posts")
]
    