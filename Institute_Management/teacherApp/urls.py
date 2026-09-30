from django.urls import path
from teacherApp.views import *

urlpatterns = [
    path('display-teachers/', display_teacher, name='display_teacher'),
    path('add-teacher/', add_teacher, name='add_teacher'),
]