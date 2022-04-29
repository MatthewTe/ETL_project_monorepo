# Importing Articles models:
from .models import Article

# Importing form methods & tinyMCE methods:
from django import forms
from tinymce.widgets import TinyMCE

# Importing custom users to be used as Author field:
from api_core.models import CustomUser  

class ArticleForm(forms.ModelForm):
    """A form model field that can be used by a frontend to create/update Articles.

    It uses the tinyMCE text editor to edit main Article content (It stores the HTML as a text field)

    """
    body = forms.CharField(widget=TinyMCE())
    class Meta:
        exclude = ("slug",)
        model = Article

    field_order = ["title", "author", "category", "body"]

    def __init__(self, *args, **kwargs):
        """Overwriting the default init field to auto fill the author field as the current user.
        """
        # Extracting the current user:
        user =kwargs.pop("user", "")
        #TODO: THis is so strange idk why this worked good lord its ugly:
        if type(user) == str:
            super(ArticleForm, self).__init__(*args, **kwargs)
        else:    
            super(ArticleForm, self).__init__(*args, **kwargs)
            self.fields["author"] = forms.ModelChoiceField(queryset=CustomUser.objects.filter(username=user.username))