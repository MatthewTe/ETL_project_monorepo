from rest_framework import routers
from django.urls import path, include

# Viewset imports:
from PROFILE_API.views import ProfileViewSet, ProfileCategoryViewSet

PROFILE_API_router = routers.DefaultRouter()

PROFILE_API_router.register(r"profiles", ProfileViewSet)
PROFILE_API_router.register(r"categories", ProfileCategoryViewSet)

urlpatterns = PROFILE_API_router.urls