# Importing Django url modules:
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

# Importing the Article Viewsets:
from .views import ArticleViewSet, ArticleCategoryViewSet

router = routers.DefaultRouter()

# Adding routes to router:
router.register(r'article_content', ArticleViewSet)
router.register(r'article_categories', ArticleCategoryViewSet)

urlpatterns = router.urls