# Importing native django methods:
from django.contrib import admin
from django.urls import path, include

# Importing DRF methods:
from rest_framework.schemas import get_schema_view
from rest_framework import permissions

# API Documentation Packages:
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Creating API Schema Documentation:
schema_view = get_schema_view(
   openapi.Info(
      title="Data APIs",
      default_version='v1',
      terms_of_service="https://www.google.com/policies/terms/",
      description="See our documentation [here](https://etl-project-monorepo.readthedocs.io/en/latest/)",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # DRF urls:
    path('api-auth/', include('rest_framework.urls')),

    # API schema:
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # Core Functionality for API Routes:
    path("api_core/", include("api_core.urls")),

    # Reddit REST API urls:
    path('reddit/', include("data_APIs.reddit_api.urls")),

    # Twitter REST API urls:
    path('twitter/', include('data_APIs.twitter_api.urls'))
]
