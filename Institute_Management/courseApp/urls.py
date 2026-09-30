from django.urls import path
from courseApp.views import *

urlpatterns = [
    # Course Category URLs
    path('display-course-categories/', display_course_category, name='display_course_category'),
    path('add-course-category/', add_course_category, name='add_course_category'),
    path('edit-course-category/<int:id>/', edit_course_category, name='edit_course_category'),
    path('delete-course-category/<int:id>/', delete_course_category, name='delete_course_category'),

    # Courses URLs
    path('display-courses/', display_course, name='display_courses'),
    path('add-course/', add_course, name='add_course'),
    path('edit-course/<int:id>/', edit_course, name='edit_course'),
    path('delete-course/<int:id>/', delete_course, name='delete_course'),
]