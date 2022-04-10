# Importing models to be filtered:
from .models import Article

# Filter imports:
from django_filters import rest_framework as filters

# Filter for Article Summaries:
class ArticleSummaryFilter(filters.FilterSet):
    """Allows Article Summaries to be filtered based on their key charecteristics. 
    Will mainly be used by front-end projects to search for specific types of articles.
    """
    title = filters.CharFilter(field_name="title", lookup_expr="contains")
    author = filters.CharFilter(field_name="author__username", lookup_expr="exact")
    category = filters.CharFilter(field_name="category__name", lookup_expr="exact")
   
    start_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="gt")
    end_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="lt")

    class Meta:
        model = Article
        fields = [
            "title",
            "body",
            "author",
            "category",
            "created_at"
        ]