from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # DRF urls:
    path('api-auth/', include('rest_framework.urls')),

    # Reddit REST API Urls:
    path('reddit/', include("data_APIs.reddit_api.urls"))

]
