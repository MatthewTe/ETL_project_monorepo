from rest_framework import routers
from django.urls import path, include

# Viewset imports:
from ARTICLE_API.views import NewsArticleViewSet, PublicationViewSet

ARTICLE_API_router = routers.DefaultRouter()

ARTICLE_API_router.register(r"news-articles", NewsArticleViewSet)
ARTICLE_API_router.register(r"publications", PublicationViewSet)

urlpatterns = ARTICLE_API_router.urls