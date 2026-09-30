from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authApp.urls')),
    path('', include('generalApp.urls')),
    path('', include('studentApp.urls')),
    path('', include('teacherApp.urls')),
    path('', include('courseApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
