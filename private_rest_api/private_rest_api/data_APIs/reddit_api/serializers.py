# Importing serializer methods:
from rest_framework import serializers

# Importing Reddit Post Models:
from .models import RedditPosts

# Abstract Serializer Objects:
class RedditPostsSerializer(serializers.HyperlinkedModelSerializer):
    
    # Explicitly Adding Primary Key to Reddit Serializer:
    id = serializers.CharField()

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(RedditPostsSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = RedditPosts
        fields = "__all__"