from authApp.views import *
from django.urls import path

urlpatterns = [
    path('', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]