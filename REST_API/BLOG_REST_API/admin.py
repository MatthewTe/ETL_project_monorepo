from django.contrib import admin

# Importing models:
from BLOG_REST_API.models import BlogPost, BlogCategory


# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogCategory)