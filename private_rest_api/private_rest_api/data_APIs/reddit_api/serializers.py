# Importing serializer methods:
from rest_framework import serializers

# Importing Reddit Post Models:
from .models import RedditPosts, Subreddit

class RedditPostsSerializer(serializers.ModelSerializer):
    # Specifying the ForeginKey field on display:
    subreddit = serializers.CharField(source="subreddit.name")

    class Meta:
        model = RedditPosts
        fields = "__all__"
        depth = 1

class SubredditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subreddit
        fields = "__all__"
        depth = 1