from django.urls import path
from studentApp.views import *

urlpatterns = [
    path('display_students/', display_student, name='display_student'),
    path('add_student/', add_student, name='add_student'),
]