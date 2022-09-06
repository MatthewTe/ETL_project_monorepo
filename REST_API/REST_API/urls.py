from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views

from rest_framework import permissions
#from rest_framework_simplejwt.views import TokenRefreshView
#from REST_API.views import CustomTokenObtainPairView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# User management urls:
from user_management.auth import APIAuthToken

# Creating the OpenAPI schema:
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # API schema patterns:
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),

    # Authentication Routes:
    #path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', views.obtain_auth_token),
    
    # BLOG REST API Routes:
    path("blog-api/", include("BLOG_REST_API.urls"))
]
