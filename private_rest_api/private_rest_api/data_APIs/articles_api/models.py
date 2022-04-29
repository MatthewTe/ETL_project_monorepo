# Importing core django methods:
from django.db import models
from django.template.defaultfilters import slugify
from tinymce import models as tinymce_models

# Importing main user model:
from api_core.models import CustomUser  

class ArticleCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Article Categories"

class Article(models.Model):
    """The main database model for written articles. It stores the main components of
    user written articles. It is designed to be connected to a CRUD API ViewSet. 

    Attributes:
        title (models.CharField): The main title for the article. It is used to generate the slug.
        
        body (tinymce_models.HTMLField): The main content of the article. It is stored as filtered HTML content using the
            tinyMCE model field that behaves as a normal TEXT field.

        author (models.ForeignKey): The author of the article that is connected via a foreign key to the
            main User model that the django project uses.

        category (models.ForeignKey): The category used to sort/filter individual articles. It is connected
            to the Category model via a foreign key.

        created_at (models.DateTimeField): The datetime that the Article was created. This field is populated 
            on model instance creation.

        last_updated (models.DateTimeField): The date time that the article was last changed.

        slug (models.SlugField): The slug for the article, generated from the article title.

    """
    title = models.CharField(max_length=250)
    body = tinymce_models.HTMLField()
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True)
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
    


