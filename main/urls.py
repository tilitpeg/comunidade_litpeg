from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('register/', login_required(views.register), name='register'),
    path('alterarSenha/', login_required(views.alterarSenha), name='alterar.senha'),
]