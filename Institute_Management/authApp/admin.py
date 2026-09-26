from django.contrib import admin
from authApp.models import UserModel, basicUserInfoModel

admin.site.register([
    UserModel,
    basicUserInfoModel
])
