from django.contrib import admin
from authApp.models import UserModel

admin.site.register([
    UserModel,
])
