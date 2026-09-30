from django.db import models
from django.core.validators import MinValueValidator
from authApp.models import UserModel

class CourseCategoryModel(models.Model):
    name = models.CharField(null=True, max_length=40)

    def __str__(self):
        return f'{self.name}'


class CourseModel(models.Model):
    title = models.CharField(null=True, max_length=100)
    description = models.TextField(null=True)
    category = models.ForeignKey(
        CourseCategoryModel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='course_category'
    )
    course_fee = models.FloatField(null=True, validators=[MinValueValidator(0.00)])
    course_module = models.TextField(null=True)
    course_thumbnail = models.ImageField(null=True, upload_to='media/course_img')
    course_credit = models.FloatField(null=True, validators=[MinValueValidator(0.00)])
    created_by = models.ForeignKey(
        UserModel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='course_creator'
    )

    def __str__(self):
        return f'{self.title}'