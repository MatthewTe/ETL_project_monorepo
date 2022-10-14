from rest_framework import serializers

# Model imports:
from ARTICLE_API.models import NewsArticle, Publication
from PROFILE_API.serializers import ProfileCategorySerializer, ProfileSerializer

# News Article Serializers:
class NewsArticleSerializer(serializers.ModelSerializer):
    # Declaring relation fields (foregin keys, many-to-many):
    category = ProfileCategorySerializer(many=True)
    authors = ProfileSerializer(many=True) 
    publisher = serializers.SlugRelatedField(queryset=Publication.objects.all(), slug_field="name")

    class Meta:
        model = NewsArticle
        fields = "__all__"

class PublicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publication
        fields = "__all__"