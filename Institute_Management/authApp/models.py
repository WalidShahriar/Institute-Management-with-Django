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

class BasicUserInfoModel(models.Model):

    name = models.CharField(null=True, max_length=100)
    address = models.TextField(null=True)
    phone = models.CharField(null=True, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
