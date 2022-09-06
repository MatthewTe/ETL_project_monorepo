from django.db import models

# Create your models here.
from django.db import models

# Blog Models - Blog and Blog Categories:
from django.template.defaultfilters import slugify
#from tinymce import models as tinymce_models - Unsure if we will use TinyMCE

# Importing main user:
from user_management.models import CustomUser

class BlogCategory(models.Model):
    "Simple model for the categories of blog posts"
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Blog Categories"


class BlogPost(models.Model):
    """The main database model for blog posts. It stores the main components of
    user written posts. It is designed to be connected to a CRUD API ViewSet. 
    
    Attributes:
        title (models.CharField): The main title for the post. It is used to generate the slug.
        
        body (models.TextField): The main content of the post. It is markdown content stored as a text field.
                        
        author (models.ForeignKey): The author of the blog post that is connected via a foreign key to the
            main User model that the django project uses.
    
        category (models.ForeignKey): The category used to sort/filter individual posts. It is connected
            to the Category model via a foreign key.
    
        created_at (models.DateTimeField): The datetime that the blog post was created. This field is populated 
            on model instance creation.
    
        last_updated (models.DateTimeField): The date time that the blog was last changed.
    
        slug (models.SlugField): The slug for the blog, generated from the blog title.

    """
    title = models.CharField(max_length=250, unique=True)
    body = models.TextField()
    # No Image functionality yet - look into adding this.
    #image = models.ImageField(null=True, blank=True, upload_to="ceteris_paribus/articles/")
    #img_source = models.CharField(null=True, blank=True, max_length=300)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        "Overwriting the save function to automatically slugify the title and set a slug value."
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    