# Django Imports:
from django.contrib import admin

# Importing Reddit Models:
from .models import RedditPosts, Subreddit, RedditDeveloperAccount

admin.site.register(RedditPosts)
admin.site.register(Subreddit)
admin.site.register(RedditDeveloperAccount)
