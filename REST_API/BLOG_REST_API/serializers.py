from rest_framework import serializers
from BLOG_REST_API.models import BlogCategory, BlogPost

from user_management.models import CustomUser

class BlogPostSerializer(serializers.ModelSerializer):
    # Specifying foreign key fields:
    author = serializers.SlugRelatedField(queryset=CustomUser.objects.all(), slug_field="username")
    category = serializers.SlugRelatedField(queryset= BlogCategory.objects.all(), slug_field="name")
    
    class Meta:
        model = BlogPost
        fields = "__all__"


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"