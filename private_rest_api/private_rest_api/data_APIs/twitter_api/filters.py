# Importing Twitter models to be filtered: 
from .models import TrendingTwitterTopic

# Filter imports:
from django_filters import rest_framework as filters

class TrendingTwitterTopicFilter(filters.FilterSet):
    """A Django Filterset for the Trending Twitter Posts API"""
    name = filters.CharFilter(field_name="name", lookup_expr="contains")
    location = filters.CharFilter(field_name="location__name", lookup_expr="exact")
    
    start_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="gt")
    end_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="lt")

    class Meta:
        model = TrendingTwitterTopic
        fields = [
            "name",
            "created_at",
            "location"
        ]