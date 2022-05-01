# Importing native django packages:
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

# Importing view logic:
from .article_logic import get_article_categories, get_article_summary, get_full_article

# Importing Article forms & models:
from data_APIs.articles_api.forms import ArticleForm
from data_APIs.articles_api.models import Article 

# Method that checks if user is a staff member: 
def is_not_staff(user):
    "Checks if the user is a staff member. This method is used in permission decorators."
    return user.is_staff

# Homepage Views:
def render_homepage(request):
    """Function that renders the main homepage for the frontend. 
    
    In order to populate the homepage it requires article data queried from 
    the backend.

    """
    context = {}

    # Querying articles from backend:
    articles = get_article_summary(page_size=5)
    context["articles"] = articles

    return render(request, "application_frontend/homepage/homepage.html", context=context)

# Article Views:
def render_article_homepage(request):
    """View that renders the homepage for articles
    
    - Query Categories.
    - Extract top 6 articles for each category
    """
    # Creating context to populate:
    context = {}

    # Extracting all Article Categories:
    categories = get_article_categories()
    context["categories"] = {}

    # Extrating the 6 most recent articles for each cateogry and adding them to an iterable array in context:
    for category in categories:
        article_summary = get_article_summary(category=category)        
        context["categories"][category] = article_summary

    return render(request, "application_frontend/articles/articles_homepage_layout.html", context=context)

def render_article_full(request, slug:str):
    """The view that renders a full article based on a slug field provided.
    """
    context = {}
    
    # Querying article based on slug and adding article to context:
    article = get_full_article(slug)
    context["article"] = article

    return render(request, "application_frontend/articles/full_article.html", context=context)

def render_article_category(request, category:str):
    """The view that renders the front-end template for dispalying all articles within a specific category.

    Args:
        category (str): The category that will be used to filter all articles.
    
    """
    context = {}
    # Making request for article summaries based on the category provided:
    articles = get_article_summary(category=category, page_size=50)
    context["articles"] = articles

    return render(request, "application_frontend/articles/article_category_page.html", context=context)


@user_passes_test(is_not_staff)
def create_article(request, id=None):
    """The view that contains the logic for creating a new article or for editing one if it already exists.

    The view uses the traditional logic from django model forms for editing existing articles and creating new
    ones. The core logic centers around the form.save() function. There are two main url paths that use this view.
    If an 'id' url param is provided (the primary key for articles in the database) then an existing article is being
    edited. If no id param is provided then a new article instance is being created.

    As it has not been decided if this front-end application will be seperated from the main back-end data ingestion 
    application these views have been written in a manner where they can easily be converted to a stand-alone project.
    This is why most of the article based views rely on external 'article logic' methods as these an be swapped from 
    using back-end querying through the native django ORM to performing REST API calls. If this move is done there are
    some ORM calls and logic in this method that only work because it is part of the same project. If the frontend is
    migrated this will have to change.

    """
    context = {}
    # Logic for initial request - creting the form object:
    if request.method == "GET":
        
        # If no id value is provided, render the template with an unpopulated form:
        if id == None:
            form = ArticleForm(user=request.user)
            context["form"] = form
            return render(request, "application_frontend/articles/create_articles.html", context=context)

        # Pre-populating the form fields with article indicated by the id:
        else:
            # Querying article:
            article = Article.objects.get(id=id)
            # Creating the article form pre-poluated with existing fields:
            initial = {
                "title": article.title,
                "author": article.author,
                "category": article.category,
                "body": article.body
            }
            form = ArticleForm(initial=initial)
            context["form"] = form

            return render(request, "application_frontend/articles/create_articles.html", context=context)
    
    # Processing form inputs. An id fields indicates if an Article object is created or updated:
    #TODO: If this application is mirgated to another project - change this to a REST based ingestion:
    elif request.method == "POST":
        # If a form is to be created:
        if id == None:
            form = ArticleForm(request.POST)
            # Validating and saving the article:
            if form.is_valid():
                article = form.save()
                # Redirecting to the newly created article:
                return redirect("full_article", slug=article.slug)

        # If a form is used to edit an existing article:
        else:
            # Querying the article to use as an instance in the model form:
            existing_article = Article.objects.get(id=id)
            form = ArticleForm(request.POST, instance=existing_article)
            if form.is_valid():
                article = form.save()
                # Redirecting to the newly created article:
                return redirect("full_article", slug=article.slug)

# Dashboard Views:
def render_dashboard_homepage(request):
    """View that renders the homepage for data dashboards"""
    return render(request, "application_frontend/data_dashboards/data_dashboard_layout.html", context={})

# Korea Views:
def render_north_korea_homepage(request):
    """View that renders the homepage for the North Korea homepage"""
    return render(request, "application_frontend/north_korea/north_korea_homepage_layout.html", context={})


# Documentation Views:
def render_documentation_homepage(request):
    """View that renders the homepage for the API Documentation"""
    return render(request, "application_frontend/documentation/api_documentation_homepage.html", context={})

def render_about_page(request):
    """View that renders the about page"""
    return render(request, "application_frontend/documentation/about_page.html", context={})