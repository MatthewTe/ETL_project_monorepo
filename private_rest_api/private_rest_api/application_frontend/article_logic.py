# Importing article models, filters and seralizers:
from data_APIs.articles_api.models import Article, ArticleCategory
from data_APIs.articles_api.filters import ArticleSummaryFilter
from data_APIs.articles_api.serializers import ArticleSummarySerializer, ArticleSerializer



# Create method that extracts the necessary logic for extracting articles:
def get_article_summary(**kwargs):
    """A method that extracts and returns article summaries from the database. 

    The method takes in all query inputs necessary to filter the article dataset. The reason
    that this method is used by the view method to query article data as opposed to querying
    the data via native django tools is for the puropse of modularity. 
    
    Currently this method operates as part of the backend django project. If the app is removed 
    from the backend project and included in its own frontend django project then the querying
    logic can be changed from using internal data models and native django ORM queires to use of 
    the ETL data API. If this is the case then this documentation needs to be removed.

    Kwargs:
        title (string): The main title for the article. It is used to generate the slug.
        
        author (strong): The author of the article.

        category (string): The category used to sort/filter individual articles. 

        start_date (string): Only articles created on or after this date will be returned.

        end_date (string): Only articles created on or before this date will be returned.

    Returns:
        dict: The dictionary containing all the seralized summary information of the articles queried.
    """
    # Extracting key work arguments/creating them if not persent:
    if "page_size" not in kwargs:
        kwargs["page_size"] = 6
    
    # Querying all articles to be filtered based on kwargs:
    queryset = Article.objects.all()
    filterset = ArticleSummaryFilter(kwargs, queryset=queryset)
    
    if filterset.is_valid():
        queryset = filterset.qs

    # Extracting the top 6 articles from the filtered queryset and seralizing them into JSON objects:
    queryset = queryset[0: (kwargs["page_size"] + 1) ]     
    seralized_queryset = ArticleSummarySerializer(queryset, many=True)

    return seralized_queryset.data

def get_article_categories():
    """A method that extracts and returns all the categories from the database.
    
    The reason that this method is used by the view method to query article data as opposed to 
    querying the data via native django tools is for the puropse of modularity. 
    
    Currently this method operates as part of the backend django project. If the app is removed 
    from the backend project and included in its own frontend django project then the querying
    logic can be changed from using internal data models and native django ORM queires to use of 
    the ETL data API. If this is the case then this documentation needs to be removed
    
    Returns:
        list: A list of all the available categories returned from the query
    """
    # Internal ORM query logic:
    categories = [category.name for category in ArticleCategory.objects.all()]

    return categories
    
def get_full_article(slug:str):
    """A method that extracts an returns the full content of a single article. 

    It returns the full HTML content as a string. The reason that this method is used 
    by the view method to query article data as opposed to querying the data via native 
    django tools is for the puropse of modularity. 
    
    Currently this method operates as part of the backend django project. If the app is removed 
    from the backend project and included in its own frontend django project then the querying
    logic can be changed from using internal data models and native django ORM queires to use of 
    the ETL data API. If this is the case then this documentation needs to be removed

    Args:
        slug (str): The string that is used to identify the individual article

    Returns:
        dict: A dictionary containing the full article contents that are returned from the query.
    
    """
    # Querying the article based on the provided slug:
    article = Article.objects.get(slug=slug)

    # Seralizing the article:
    seralized_article = ArticleSerializer(article)

    return seralized_article.data

def create_full_article(author, category, body):
    """The method that creates a new article in the database given the key params.

    Currently this method operates as part of the backend django project. If the app is removed 
    from the backend project and included in its own frontend django project then the querying
    logic can be changed from using internal data models and native django ORM queires to use of 
    the ETL data API. If this is the case then this documentation needs to be removed

    Args:
        author (str): The author of the article that corresponds to a backend user.

        category (str): The category of the article that corresponds to the backend category.name field.

        body (str): The large text field containing the HTML content of the full article content.
    
    
    """
    pass