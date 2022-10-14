from django.db import models

# Genertic Category Model:
class ProfileCategory(models.Model):
    "A generic model for categories used by many other models"
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Profile Categories"

# Main profile data model: 
class Profile(models.Model):
    "The main model representing personel profiles that connects to other models"
    # Basic info:
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Connecting BLOG post categories:
    category = models.ManyToManyField(ProfileCategory, blank=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    class Meta:
        verbose_name_plural = "Profiles"

