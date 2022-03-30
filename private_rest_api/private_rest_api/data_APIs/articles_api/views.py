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
from .serializers import ArticleSerializer, ArticleSummarySerializer, ArticleCategorySerializer

# Importing schema documentation methods:
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# TODO: Add openapi documentation for ArticleViewSet
# TODO: Add pagination and filtering to the ArticleViewSet list() function.
# TODO: Decide if HTML needs to be escaped in the POST request or in the retrieve function.

# TODO: Add documentation for ArticleCategoryViewSet.
# TODO: Add openapi documentation for the ArticleCategoryViewSet.
# TODO: For all 400 errors, seralize and include error msg in the Response object

class ArticleViewSet(viewsets.ViewSet):
    """The main viewset for performing CRUD functions on the Article model.
    
    The object deals with the full CRUD operations for the Article model and appropriate Article 
    authentication/permissions.

    """
    queryset = Article.objects.all()
    #serializer_class = ArticleSerializer
    lookup_field = "slug"

    @swagger_auto_schema(operation_description="Placeholder for list() GET endpoint schema.")
    def list(self, request):
        """The method that recives a GET request and returns multiple article summary objects.

        The GET requests results in a paginated and filtered JSON response of summary article data. This
        summary data is created by passing the main Article queryset through the ArticleSummarySerializer 
        instead of the ArticleSerializer. This ommits the main body content from each Article object.

        The purpose of this endpoint is to provide a way for front-end services to query 'thumbnails' of
        articles.

        Args:
            request (request): The HTTP request object recieved from the query.

        Returns:
            rest_framework.response.Response: The HTTP response containing the Article Sumamry data as JSON.
        """
        # Creating the main queryset:
        queryset = Article.objects.all()

        # Seralizing the Article Queryset through the Summary Serializer to create a summary dataset:
        seralized_queryset = ArticleSummarySerializer(queryset, many=True, context={'request':request})
        
        return Response(seralized_queryset.data, status=status.HTTP_202_ACCEPTED)
    
    @swagger_auto_schema(operation_description="Placeholder for POST request endpoint schema.")
    def create(self, request):
        """The method that proceses the POST request used to create Article objects and store them in the 
        database.

        The method requires the content of the Article to be passed as a dictionary in the request body. It
        extracts this body content and uses it to create an Article database object. For foreign key fields
        the method queries the respective objects based on the query param provided in the request. 

        For the ArticleCategory foreign key, if a corresponding category is not found, a new ArticleCategory 
        object is created using the query param and said new Cateogry object is then used as the Article's 
        foreign key.

        The fields required to create an Article object are:
            
            title (str): The article title
            
            body (str): The HTML body content that is escaped in order to prevent malicious injection.

            author (str): The author of the post, which must correspond to a CustomUser instance via its
                username field.
            
            category (str): The main category the article falls under. This value corresponds with the 'name'
                field of an ArticleCategory object. If it does not, a new ArticleCategory object is created.

        Args:
            request (request): The HTTP POST request object recieved from the query.

        Returns:
            rest_framework.response.Response: The HTTP response containing the newly created article object.

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
    
    @swagger_auto_schema(operation_description="Placeholder for the single Artilce GET request endpoint.")
    def retrieve(self, request, slug=None):
        """The method that processes a GET request to the article_content endpoint and returns a single 
        serialized Article object based on the slug specified in the url.

        Args:
            request (request): The GET request object recieved from the query.

            slug (str): The slug field that corresponds to the Article returned.

        Returns:
            rest_framework.response.Response: The HTTP response object containing the Article full content.
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
    
    @swagger_auto_schema(operation_description="Placeholder for PUT request endpoint schema.")
    def update(self, request, slug=None):
        """The method that processes PUT requests to the API allowing Article objects specified by the 
        slug field to be created or updated.

        The method contains the main logic for creating an article if one does not exist with the provided slug
        field from the method that deals with POST requests - 'create()'. If an article does exist with the provided
        slug field then that article is fully updated using the body params provided in the request.

        Because this method processes PUT requests, it requires all Article fields necessary to create a new article to be
        present in the request body to sucessfully update/create an Article instance.
        
        These fields are:

            title (str): The article title
            
            body (str): The HTML body content that is escaped in order to prevent malicious injection.

            author (str): The author of the post, which must correspond to a CustomUser instance via its
                username field.
            
            category (str): The main category the article falls under. This value corresponds with the 'name'
                field of an ArticleCategory object. If it does not, a new ArticleCategory object is created.

        Any fields in the request body that differ from the fields found in the Article instance will be updated. This
        is done via the django model method 'update_or_create()'. 
        
        Args:
            request (request): The PUT request object recieved from the query.

            slug (str): The slug field that corresponds to the Article to be created or updated..

        Returns:
            rest_framework.response.Response: The HTTP response object containing the new or updated article along with
                a boolean indicated if a new article has been created or if an existing one has been updated. 

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

    @swagger_auto_schema(operation_description="Placeholder for PATCH request endpoint schema.")
    def partial_update(self, request, slug=None):
        """The method that processes the PATCH request sent to the article_content endpoint and allows an Article
        instance to be edited based on the slug provided.

        This method, unlike the 'update()' method only processes PATCH requests meaning it does not allow for the
        creation of a new Article instance if there is no corresponding article with the provided slug field. The 
        method also does not require all Article fields to be provided in the request body to update an existing
        instance. Only the Article fields that are present in the request body will be updated.
        
        Args:
            request (request): The PATCH request object recieved from the query.

            slug (str): The slug field that corresponds to the Article being updated.

        Return:
            rest_framework.response.Response: The HTTP response object containing the Article that has been updated.

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
    
    @swagger_auto_schema(operation_description="Placeholder for DELETE request endpoint schema.")
    def destroy(self, request, slug=None):
        """The method that processes DELETE requests made to the article_content endpoint and deletes 
        an Article instance based on the provided slug field.

        Args:
            request (request): The DELETE request object recieved from the query.

            slug (str): The slug field that corresponds to the Article being deleted.

        Returns:
            rest_framework.response.Response: The HTTP response object containing the Article that has been deleted.

        """
        # Querying article based on slug to remove:
        article = Article.objects.get(slug=slug)
        
        # Serializing the article to return in the response:
        serialized_article = ArticleSerializer(article, context={'request':request})
        article.delete()

        return Response(serialized_article.data, status=status.HTTP_202_ACCEPTED)

class ArticleCategoryViewSet(viewsets.ViewSet):
    """The viewset for performing limited CRUD functions on the Article Category model.

    It only performs limited CRUD operations as some additional functionality such as the 'partial update'
    functions are not necessary for the API

    """
    queryset = ArticleCategory.objects.all()
    lookup_field = "name"

    @swagger_auto_schema(operation_description="Placeholder for list() GET endpoint schema.")
    def list(self, request):
        """The method receives the GET request for the article categories endpoint and returns
        all seralized article categories.

        Args:
            request (request): The GET request object recieved from the query.

        Returns:
            rest_framework.response.Response: The HTTP response object containing all seralized Article Category objects.

        """
        # Querying all article categories:
        categories = ArticleCategory.objects.all()

        # Serializing the Category objects:
        serialized_categories = ArticleCategorySerializer(categories, many=True, context={'request':request})

        return Response(serialized_categories.data, status=status.HTTP_202_ACCEPTED)
    
    @swagger_auto_schema(operation_description="Placeholder for POST request endpoint schema.")
    def create(self, request):
        """The method that receives the POST request for the article categories endpoint and creates
        an Article Category object based on the request body parameters.

        Args:
            request (request): The HTTP POST request object recieved from the query.

        Returns:
            rest_framework.response.Response: The HTTP response object containing the Category object that has been created.

        """
        # Extracting params from request body to create Article object:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Extracting body fields:
        name = body["name"]

        try:
            # Creating the new Category:
            category = ArticleCategory.objects.create(name=name)

            # Serializing Category object to be returned via the response:
            serialized_category = ArticleCategorySerializer(category, context={"request":request})            
            
            return Response(serialized_category.data, status=status.HTTP_202_ACCEPTED)
        
        except Exception as error:
            print(error)
            return Response(status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(operation_description="Placeholder for PUT requests endpoint schema.")
    def update(self, request, name=None):
        """The method that recieves PUT requests and updates the Article Category object specified by 
        the provided name field based on the body content of the incoming request. 

        It processes PUT requests not PATCH requests so all categroy fields need to be provided in the
        request body for the Category object to be updated.
                
        These fields are:

            name (str): The name of the Category
            
        Any fields in the request body that differ from the fields found in the Category instance will be updated. This
        is done via the django model method 'update_or_create()'. 
        
        Args:
            request (request): The PUT request object recieved from the query.

            name (str): The name field that corresponds to the Article to be created or updated.
        
        Returns:
            rest_framework.response.Response: The HTTP response object containing the new or updated Category along with
                a boolean indicated if a new Category has been created or if an existing one has been updated.

        """
        # TODO: Add body param extraction logic once more fields get added to the Category model.
        # Extracting body params used to update the 
        #body_unicode = request.body.decode('utf-8')
        #body = json.loads(body_unicode)

        # Performing an update or create operation for a category:
        obj, created_status = ArticleCategory.objects.update_or_create(
            name=name,

            defaults = {
            }
        )
        # Serializing the article that has been updated to return in a request:
        serialized_article = ArticleCategorySerializer(obj, context={'request':request})

        return Response(
            {
                "Created": created_status,
                "Article": serialized_article.data
            }, 
            status=status.HTTP_202_ACCEPTED)

    @swagger_auto_schema(operation_description="Placeholder for DELETE request endpoint schema.")
    def destroy(self, request, name=None):
        """The method that recieves the DELETE request and removes the Article Category object from
        the database specified by the name param.

        Args:
            request (request): The DELETE request object recieved from the query.
            
            name (str): The name of the Category to be deleted.

        Returns:
            rest_framework.response.Response: The Response object containing the Category object deleted. 
        """
        # Querying the category object:
        category = ArticleCategory.objects.get(name=name)

        # Serializing the article to return in the response:
        serialized_category = ArticleCategorySerializer(category, context={'request':request})
        category.delete()

        return Response(serialized_category.data, status=status.HTTP_202_ACCEPTED)

