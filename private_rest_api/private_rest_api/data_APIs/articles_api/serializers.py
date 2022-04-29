# Importing serializer methods:
from rest_framework import serializers

# Importing Article Models: 
from .models import Article, ArticleCategory

class ArticleSerializer(serializers.ModelSerializer): 
    # Specifying foreign key fields:
    author = serializers.CharField(source="author.username")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Article
        fields = "__all__"
        depth = 1

class ArticleSummarySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField(source="author.username")
    category = serializers.CharField(source="category.name")
    created_at = serializers.DateTimeField()
    last_updated = serializers.DateTimeField()
    slug = serializers.CharField()
    
    class Meta:
        model = Article
        fields = ["title", "author", "category", "created_at", "last_updated", "slug", "id"]
        depth = 1

class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = "__all__"
        depth = 1