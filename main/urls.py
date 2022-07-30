from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.HomeView), name='home'),
    path('accounts/register', views.register, name='register'),
]