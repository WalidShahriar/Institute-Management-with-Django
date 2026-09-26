from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):

    USER_TYPES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin')
    ]

    user_type = models.CharField(null=True, max_length=50, choices=USER_TYPES)

    def __str__(self):
        return f'{self.username}'
