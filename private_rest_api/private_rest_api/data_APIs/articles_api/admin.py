from django.contrib import admin

# Importing Article models: 
from .models import Article, ArticleCategory

admin.site.register(Article)
admin.site.register(ArticleCategory)

