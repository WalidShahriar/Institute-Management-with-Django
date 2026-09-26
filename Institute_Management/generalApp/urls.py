from generalApp.views import *
from django.urls import path


urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard')
]