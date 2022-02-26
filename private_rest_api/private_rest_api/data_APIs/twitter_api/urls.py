# Importing native django methods:
from django.contrib import admin
from django.urls import path, include

# Importing views:
from .views import trending_twitter_topics

urlpatterns = [
    path(r"trending/", trending_twitter_topics, name="Trending Topics") 
]