# Importing native django methods:
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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
    # Frontend urls:
    path("", include("application_frontend.urls")),
    
    # Login/Logout urls:
    path("login/", auth_views.LoginView.as_view(template_name="api_core/login.html"), name="main_login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="api_core/logout.html"), name="main_logout"),

    # Admin:
    path('admin/', admin.site.urls),

    # TinyMCE (text-editor) urls:
    path('tinymce/', include('tinymce.urls')),

    # DRF urls:
    path('api-auth/', include('rest_framework.urls')),

    # API schema:
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Plotly-Dash urls:
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    
    # Core Functionality for API Routes:
    path("api_core/", include("api_core.urls")),

    # Reddit REST API urls:
    path('reddit/', include("data_APIs.reddit_api.urls")),

    # Twitter REST API urls:
    path('twitter/', include('data_APIs.twitter_api.urls')),

    # Articles REST API urls:
    path('articles/', include("data_APIs.articles_api.urls")), 

]

# Adding development url for uploading and accessing images:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Defining a custom 404 page error handeling function:
handler404 = "private_rest_api.views.page_not_found_view"