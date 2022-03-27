from django.shortcuts import render
from django.template.defaultfilters import slugify

# Importing DRF methods:
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Importing data manipulation packages:
import json

# Importing article models and serializers:
from api_core.models import CustomUser
from .models import Article, ArticleCategory
from .serializers import ArticleSerializer, ArticleSummarySerializer

# TODO: Add documentation for the CRUD functions for Articles.
# TODO: Add openapi documentation for ArticleViewSet

# TODO: Populate a ArticleCategoryViewSet with only list, create, destroy. 
# TODO: Add documentation for ArticleCategoryViewSet.
# TODO: Add openapi documentation for the ArticleCategoryViewSet.

class ArticleViewSet(viewsets.ViewSet):
    """The main viewset for performing CRUD functions on the Article model.
    
    The object deals with the full CRUD operations for the Article model and appropriate Article authentication/permissions.

    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"

    def list(self, request):
        """
        """
        # Creating the main queryset:
        queryset = Article.objects.all()

        # Seralizing the Article Queryset through the Summary Serializer to create a summary dataset:
        seralized_queryset = ArticleSummarySerializer(queryset, many=True, context={'request':request})
        
        return Response(seralized_queryset.data, status=status.HTTP_202_ACCEPTED)

    def create(self, request):
        """
        """
        # Extracting params from request body to create Article object:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        title = body["title"]
        body_content = body["body"]
        
        # Extracting the author component and querying the User object:
        try:
            author = CustomUser.objects.get(username=body["author"])
        except Exception as error:
            print(error)
            return Response(status=status.HTTP_404_NOT_FOUND)

        # ^ Doing the same for the Category component:
        try:
            if ArticleCategory.objects.get(name=body["category"]).exists():
                category = ArticleCategory.objects.get(name=body["category"])
            else:
                category = ArticleCategory.objects.create(name=body["category"])
        except Exception as error:
            print(error)
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Creating article object from extracted params:
        try:
            new_article = Article.objects.create(
                title=title,
                body=body_content,
                author=author,
                category=category
            )
            
            # Serializing the new article to be passed onto the Request:
            serialized_article = ArticleSerializer(new_article, context={'request':request})

            return Response(serialized_article.data, status=status.HTTP_202_ACCEPTED)

        except Exception as error:
            print(error)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, slug=None):
        """
        """
        if slug is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # Querying the single article based on the slug parameter:
        try:
            article = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Serializing the article and adding it to the Response:
        serialized_article = ArticleSerializer(article, context={'request':request})

        return Response(serialized_article.data, status=status.HTTP_202_ACCEPTED)

    def update(self, request, slug=None):
        """
        """
        # Extracting body params used to update the 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Extracting the author component and querying the User object:
        try:
            author = CustomUser.objects.get(username=body["author"])
        except Exception as error:
            print(error)
            return Response(status=status.HTTP_404_NOT_FOUND)

        # ^ Doing the same for the Category component:
        try:
            if ArticleCategory.objects.get(name=body["category"]).exists():
                category = ArticleCategory.objects.get(name=body["category"])
            else:
                category = ArticleCategory.objects.create(name=body["category"])
        except Exception as error:
            print(error)
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Performing an update or create operation for an Article:
        
        obj, created_status = Article.objects.update_or_create(
            slug=slug,

            defaults = {
                "title": body["title"],
                "body": body["body"],
                "author": author,
                "category": category
            }
        )
        # Serializing the article that has been updated to return in a request:
        serialized_article = ArticleSerializer(obj, context={'request':request})

        return Response(
            {
                "Created": created_status,
                "Article": serialized_article.data
                }, 
            status=status.HTTP_202_ACCEPTED)

    def partial_update(self, request, slug=None):
        """
        """
        # Loading the body params from the request to update the request:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Querying single Article for updating:
        try:
            article = Article.objects.get(slug=slug)
        except Exception as error:
            print(error)
            return Response(status=status.HTTP_404_NOT_FOUND) 
        
        # Extracting content from request body and using original article values if absent:
        title = body.get("title", article.title)
        body_content = body.get("body", article.body)

        # Author value filtering to get Foreign Key connection:
        if "author" in body:
            try:
                author = CustomUser.objects.get(username=body["author"])
            except Exception as error:
                print(error)
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            author = article.author

        # Category value filtering to get Foreign Key connection:
        if "category" in body:
            try:
                category = ArticleCategory.objects.get(name=body["category"])
            except Exception as error:
                print(error)
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            category = article.category

        # Setting article variables to update the main Article object:
        article.title = title
        article.body = body_content
        article.author = author
        article.category = category

        article.save()

        # Serializing the newly updated article to attach to response:
        serialized_article = ArticleSerializer(article, context={"request":request})

        return Response(serialized_article.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, slug=None):
        """
        """
        # Querying article based on slug to remove:
        article = Article.objects.get(slug=slug)
        
        # Serializing the article to return in the response:
        serialized_article = ArticleSerializer(article, context={'request':request})
        article.delete()

        return Response(serialized_article.data, status=status.HTTP_202_ACCEPTED)

class ArticleCategoryViewSet(viewsets.ViewSet):
    """
    """
    def list(self, request):
        pass

    def create(self, request):
        pass

    def update(self, request):
        pass

    def destroy(self, request):
        pass