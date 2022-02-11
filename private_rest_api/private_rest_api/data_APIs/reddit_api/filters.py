# Importing models to be filtered:
from .models import RedditPosts 

# Filter imports:
from django_filters import rest_framework as filters

class RedditPostFilter(filters.FilterSet):
    """Generic django-filter FilterSet for the RedditPosts API."""
    title = filters.CharFilter(field_name="title", lookup_expr="contains")
    content = filters.CharFilter(field_name="content", lookup_expr="contains")
    subreddit = filters.CharFilter(field_name="subreddit__name", lookup_expr="exact")
    
    start_date = filters.DateTimeFilter(field_name="created_on", lookup_expr="gt")
    end_date = filters.DateTimeFilter(field_name="created_on", lookup_expr="lt")

    class Meta:
        model = RedditPosts
        fields = [
            "title",
            "subreddit",
            "content",
            "created_on"
        ]