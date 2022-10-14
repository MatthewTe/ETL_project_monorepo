from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

# MVC Imports:
from ARTICLE_API.models import NewsArticle, Publication
from ARTICLE_API.serializers import NewsArticleSerializer, PublicationSerializer

class NewsArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer