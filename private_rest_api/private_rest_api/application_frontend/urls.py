from django.urls import path

from .views import (
    render_homepage, render_article_homepage, render_dashboard_homepage, render_north_korea_homepage, 
    render_documentation_homepage, render_about_page, render_article_full, render_article_category, 
    create_article, render_developer_documentation
    )

urlpatterns = [
    path("", render_homepage, name="homepage"),

    path("paribus/articles", render_article_homepage, name="articles_homepage"),
    path("paribus/articles/full/<str:slug>", render_article_full, name="full_article"),
    path("paribus/articles/create", create_article, name="create_article"),
    path("paribus/articles/create/<int:id>", create_article, name="create_article"),
    path("paribus/articles/category/<str:category>", render_article_category, name="article_category"),

    path("paribus/dashboards", render_dashboard_homepage, name="dashboard_homepage"),

    path("paribus/north_korea", render_north_korea_homepage, name="north_korea_homepage"),

    # Docs section:
    path("paribus/documentation", render_documentation_homepage, name="documentation_homepage"),
    path("paribus/documentation/dev", render_developer_documentation, name="developer_documentation"),

    path("paribus/about", render_about_page, name="about_page")
    
]