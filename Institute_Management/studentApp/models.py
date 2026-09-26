from django.db import models
from authApp.models import UserModel, BasicUserInfoModel


class StudentModel(BasicUserInfoModel):

    user = models.OneToOneField(
        UserModel,
        null=True,
        on_delete=models.CASCADE
    )
    roll_no = models.CharField(null=True, max_length=20)
    image = models.ImageField(null=True, upload_to='media/student_img')


