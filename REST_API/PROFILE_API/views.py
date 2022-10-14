from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

# MVC imports:
from PROFILE_API.models import Profile, ProfileCategory
from PROFILE_API.serializers import ProfileSerializer, ProfileCategorySerializer

class ProfileViewSet(viewsets.ModelViewSet):
    "The main viewset for CRUD functionality for the Profile model"
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 

class ProfileCategoryViewSet(viewsets.ModelViewSet):
    "A generic viewswet for CRUD functionality for the Profile Category"
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = ProfileCategory.objects.all()
    serializer_class = ProfileCategorySerializer
