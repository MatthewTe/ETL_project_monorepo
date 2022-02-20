# Native Django Imports:
from django.shortcuts import render
from django.http import JsonResponse

# DRF Imports:
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination

# Create your views here.
@api_view(('GET',))
def test(request):
    return Response({"test"}, status=status.HTTP_200_OK)