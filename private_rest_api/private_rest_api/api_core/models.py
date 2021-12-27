# Native Django Imports:
from django.contrib.auth.models import AbstractUser

# Custom User for future-proofing / best practices:
class CustomUser(AbstractUser):
    pass
