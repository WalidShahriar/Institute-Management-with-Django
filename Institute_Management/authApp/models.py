from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):

    username = models.CharField(null=True, max_length=50)
    email = models.EmailField(null=True)

