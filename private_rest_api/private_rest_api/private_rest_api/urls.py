# Importing native django methods:
from django.contrib import admin
from django.urls import path, include

# Importing DRF methods:
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # DRF urls:
    path('api-auth/', include('rest_framework.urls')),

    # API schema:
    path("", include_docs_urls(title="Data APIs")),
    path("schema", get_schema_view(
        title="Data APIs",
        description="Lorem Ipsum",
        version="0.0.1"), 
        name="openapi-schema"),

    # Reddit REST API Urls:
    path('reddit/', include("data_APIs.reddit_api.urls"))

]
