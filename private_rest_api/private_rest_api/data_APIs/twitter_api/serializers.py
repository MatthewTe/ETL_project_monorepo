# Importing serializer methods:
from rest_framework import serializers

# Importing Twitter models: 
from .models import TrendingTwitterTopic

class TrendingTwitterTopicSerializer(serializers.ModelSerializer):
    # Specifying the ForeginKey field on display:
    location = serializers.CharField(source="location.name")

    class Meta:
        model = TrendingTwitterTopic
        fields = "__all__"
        depth = 1

