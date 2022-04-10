# Importing pagination methods:
from rest_framework import pagination

# Paginator for article summary content:
class ArticleSummaryPagination(pagination.PageNumberPagination):
    """Overrides the default PageNumberPagination to allow for user specific
    query sizes.
    """
    page_size = 100
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 1000