# Importing Django url modules:
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

# Importing Reddit API Viewsets:
from .views import RedditPostViewSet

# Adding reddit REST API routes to the router:
router.register(r"posts", RedditPostViewSet)

# Creating Automatic URL Routing:
urlpatterns = router.urls
    