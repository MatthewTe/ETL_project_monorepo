# Importing native django methods:
from django.contrib import admin
from django.urls import path, include

# Importing views:
from .views import test

urlpatterns = [
    path(r"trending/", test, name="Trending Topics") 
]