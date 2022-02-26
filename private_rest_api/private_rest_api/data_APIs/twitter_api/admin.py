from django.contrib import admin

# Importing models: 
from .models import TwitterDeveloperAccount, TrendingTwitterTopic, TwitterRegion

# Register your models here.
admin.site.register(TwitterDeveloperAccount)
admin.site.register(TrendingTwitterTopic)
admin.site.register(TwitterRegion)
