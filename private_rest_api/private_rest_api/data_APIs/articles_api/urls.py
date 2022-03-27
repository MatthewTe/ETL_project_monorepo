# Importing Django url modules:
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

# Importing the Article Viewsets:
from .views import ArticleViewSet

router = routers.DefaultRouter()

# Adding routes to router:
router.register(r'article_content', ArticleViewSet)

urlpatterns = router.urls