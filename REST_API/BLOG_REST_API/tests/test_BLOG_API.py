from django.test import TestCase
from django.forms.models import model_to_dict
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import RequestsClient
from django.template.defaultfilters import slugify
from rest_framework.test import APITestCase
from django.urls import reverse

# Importing modules to test:
from user_management.models import CustomUser
from BLOG_REST_API.models import BlogCategory, BlogPost
from BLOG_REST_API.serializers import BlogCategorySerializer, BlogPostSerializer

# Importing data manipulation packages:
import json
from datetime import datetime


class BlogCategoryModelTestCase(TestCase):
    "Tests the creation of BlogCategory models"
    def setUp(self):
        print("\n------------------------------------------------------------------------------------")
        print("\nRunning Setup for Blog Category Testing")

        # Loading test data:
        self.test_data = json.load(open("BLOG_REST_API/tests/test_data.json"))

        # Creating objects from test data:
        for test_object in self.test_data["BlogCategory"]:
            BlogCategory.objects.create(name=test_object["name"])

    def test_model_creation(self):
        "Only tests the interactions of Django Models"

        print("Testing Blog Category Model Creation")

        Politics = BlogCategory.objects.get(name="Politics")
        Economics = BlogCategory.objects.get(name="Economics")
        Python = BlogCategory.objects.get(name="Python")    

        self.assertEqual(Politics.name, "Politics")
        self.assertEqual(Economics.name, "Economics")
        self.assertEqual(Python.name, "Python")

    def test_model_seralization(self):
        "Tests the Seralization of Model data"
        
        print("Testing Blog Category Data Seralization")

        categories = BlogCategory.objects.all()
        politics_category = BlogCategory.objects.get(name="Politics")
        
        # Testing Seralization of a single object from model:
        politics_serializer = BlogCategorySerializer(politics_category)
        politics_test_data = self.test_data["BlogCategory"][0]
        self.assertEqual(politics_serializer.data, politics_test_data)

        # Testing Seralization of all objects from model:
        category_seralizer = BlogCategorySerializer(categories, many=True)
        self.assertEqual(category_seralizer.data, self.test_data["BlogCategory"])

        # Testing Seralization of object from JSON:
        json_data = self.test_data["BlogCategoryJSON"][0]
        json_seralizer = BlogCategorySerializer(data=json_data)
        self.assertEqual(json_seralizer.is_valid(), True)
        self.assertEqual(json_seralizer.validated_data, json_data)

        # Testing Seralization of multiple objects from JSON:
        json_data = self.test_data["BlogCategoryJSON"]
        json_seralizer = BlogCategorySerializer(data=json_data, many=True)
        self.assertEqual(json_seralizer.is_valid(), True)
        self.assertEqual(json_seralizer.validated_data, json_data)
        self.assertEqual(len(json_seralizer.validated_data), 2)

        # Testing incorrect seralization of an object:
        error_json_data = self.test_data["BlogCategory"][0]
        error_json_seralizer = BlogCategorySerializer(data=error_json_data)
        self.assertEqual(error_json_seralizer.is_valid(), False)
        self.assertEqual(error_json_seralizer.errors, {"name":[ErrorDetail(string='blog category with this name already exists.', code='unique')]})
        
    def test_api_requests(self):
        "Testing the interaction of the API using the requests library"
        
        """
        print("Tessting API Endpoint Interactions via Requests")

        # Declaring endpoint url and Request client for API testing:
        client = RequestsClient()
        response = client.get("http://127.0.0.1:8000/blog-api/categories/")
        print(response.text)
        print(dir(response))
        """


class BlogPostModelTestCase(TestCase):

    def setUp(self):

        print("\n------------------------------------------------------------------------------------")        
        print("Running Tests for Blog Post Model Creation")

        # Creating Users and Categories for testing model creation:
        politics_category = BlogCategory.objects.create(name="Politics")
        test_user = CustomUser.objects.create(username="test_user", password="test_pass")

        # Loading test data:
        self.test_data = json.load(open("BLOG_REST_API/tests/test_data.json"))

        # Using test data to create Blog Post objects:
        for post in self.test_data["BlogPosts"]:
            self.current_datetime = datetime.now()
            BlogPost.objects.create(
                title=post["title"],
                body=post["body"],
                author=CustomUser.objects.get(username=post["author"]),
                category=BlogCategory.objects.get(name=post["category"])
            )

    def test_model_creation(self):
        "Testing the Creation of Blog Posts"
        
        print("Testing Blog Posts Model Creation")
        
        # Querying the model key
        blog_posts = BlogPost.objects.all()

        # Compare the data dict with the JSON values:
        test_set = zip(blog_posts, self.test_data["BlogPosts"])
        
        # Not testing equivalence between primary keys:
        for post in test_set:            
            self.assertEqual(post[0].title, post[1]["title"])
            self.assertEqual(post[0].body, post[1]["body"])
            self.assertEqual(post[0].author.username, post[1]["author"])
            self.assertEqual(post[0].category.name, post[1]["category"])
            
    def test_model_seralization(self):
        "Tests the Seralization of Model data"
        
        print("Testing the Blog Post Data Seralization")

        posts = BlogPost.objects.all()

        # Testing Seralization of a single object from model:
        post_seralizer = BlogPostSerializer(posts[0])
        post_test_data = self.test_data["BlogPosts"][0]
        # Only testing certain fields:
        self.assertEqual(post_seralizer.data["title"], post_test_data["title"])
        self.assertEqual(post_seralizer.data["body"], post_test_data["body"])
        self.assertEqual(post_seralizer.data["author"], post_test_data["author"])
        self.assertEqual(post_seralizer.data["category"], post_test_data["category"])
        self.assertEqual(post_seralizer.data["slug"], slugify(post_test_data["title"]))

        
        # Testing Seralization of all objects from model:
        post_seralizer = BlogPostSerializer(posts, many=True)
        test_set = zip(post_seralizer.data, self.test_data["BlogPosts"])
        for post in test_set:
            self.assertEqual(post[0]["title"], post[1]["title"])
            self.assertEqual(post[0]["body"], post[1]["body"])
            self.assertEqual(post[0]["author"], post[1]["author"])
            self.assertEqual(post[0]["category"], post[1]["category"])
            self.assertEqual(post[0]["slug"], slugify(post[1]["title"]))
        self.assertEqual(len(post_seralizer.data), 3)


        
        # Testing Seralization of object from JSON:
        json_data = self.test_data["BlogPostsJSON"][0]
        json_seralizer = BlogPostSerializer(data=json_data)
        self.assertEqual(json_seralizer.is_valid(), True)
        self.assertEqual(json_seralizer.validated_data["title"], json_data["title"])
        self.assertEqual(json_seralizer.validated_data["body"], json_data["body"])
        self.assertEqual(json_seralizer.validated_data["author"]["username"], json_data["author"])
        self.assertEqual(json_seralizer.validated_data["category"]["name"], json_data["category"])
        
        
        # Testing Seralization of multiple objects from JSON:
        json_data = self.test_data["BlogPostsJSON"]
        json_seralizer = BlogPostSerializer(data=json_data, many=True)
        self.assertEqual(json_seralizer.is_valid(), True)
        for post in test_set:
            self.assertEqual(post[0]["title"], post[1]["title"])
            self.assertEqual(post[0]["body"], post[1]["body"])
            self.assertEqual(post[0]["author"], post[1]["author"])
            self.assertEqual(post[0]["category"], post[1]["category"])
            self.assertEqual(post[0]["slug"], slugify(post[1]["title"]))
        self.assertEqual(len(post_seralizer.data), 3)
        
        # Testing incorrect seralization of an object:
        error_json_data = self.test_data["BlogPosts"][0]
        error_json_seralizer = BlogPostSerializer(data=error_json_data)
        self.assertEqual(error_json_seralizer.is_valid(), False)
        test_error = [ErrorDetail(string='blog post with this title already exists.', code='unique')]
        self.assertEqual(error_json_seralizer.errors["title"], test_error)
    