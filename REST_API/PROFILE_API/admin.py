from django.contrib import admin

# Importing Profile models:
from PROFILE_API.models import Profile, ProfileCategory

admin.site.register(Profile)
admin.site.register(ProfileCategory)
