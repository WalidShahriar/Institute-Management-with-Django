from django.db import models
from authApp.models import UserModel, BasicUserInfoModel

class TeacherModel(BasicUserInfoModel):
    user = models.OneToOneField(
        UserModel,
        null=True,
        on_delete=models.CASCADE
    )

    id_no = models.CharField(null=True, max_length=20)
    image = models.ImageField(null=True, upload_to='media/teacher_img')

    def __str__(self):
        return f'{self.name}'
