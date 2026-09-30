from django.contrib import admin
from courseApp.models import CourseCategoryModel, CourseModel

admin.site.register([
    CourseModel,
    CourseCategoryModel
])
