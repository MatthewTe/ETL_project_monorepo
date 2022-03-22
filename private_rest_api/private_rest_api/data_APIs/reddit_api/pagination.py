# Importing pagination methods:
from rest_framework import pagination

# Creating custom pagination for Reddit API endpoint: 
class RedditEndpointPagination(pagination.PageNumberPagination):
    """A Pagination object that overrides the default PageNumberPagination to allow for
    user specified query sizes. 
    """
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000