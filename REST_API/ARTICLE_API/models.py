from django.db import models

# Importing Profiles for use in Article models: 
from PROFILE_API.models import Profile, ProfileCategory

# Basic publication object:
class Publication(models.Model):
    "Generic model for publications"
    name = models.CharField(max_length=100)

# Model for new article object:
class NewsArticle(models.Model):
    "The main database object for storing News Article data"
    title = models.CharField(max_length=100) 
    created_on = models.DateTimeField(blank=True, null=True)
    category = models.ManyToManyField(ProfileCategory,blank=True)
    authors = models.ManyToManyField(Profile, blank=True)
    publisher = models.ForeignKey(Publication, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News Articles"