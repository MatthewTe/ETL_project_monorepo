from rest_framework import routers
from rest_framework import routers
from django.urls import path, include

# Importing ViewSets for Routers:
from BLOG_REST_API.views import BlogPostViewSet, BlogCategoryViewSet

BLOG_REST_API_router = routers.DefaultRouter()

BLOG_REST_API_router.register(r'posts', BlogPostViewSet)
BLOG_REST_API_router.register(r'categories', BlogCategoryViewSet)

urlpatterns = BLOG_REST_API_router.urls