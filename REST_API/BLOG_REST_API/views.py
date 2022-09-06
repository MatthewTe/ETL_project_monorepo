from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

# Importing local MVC:
from BLOG_REST_API.models import BlogPost, BlogCategory
from BLOG_REST_API.serializers import BlogCategorySerializer, BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    "The main viewset for performing CRUD functions on the Blog Post model"
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogCategoryViewSet(viewsets.ModelViewSet):
    "The main viewset for performing CRUD functions on the Blog Category model"
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer