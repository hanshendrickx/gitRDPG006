# from django.db import models

# Create your models here. https://docs.djangoproject.com/en/2.2/topics/db/models/
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass