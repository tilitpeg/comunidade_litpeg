
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('main.urls')),
    path('', include('laboratorio.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
