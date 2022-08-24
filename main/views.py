from multiprocessing import context
from turtle import update
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

from main.forms import NovoUsuarioForm


def register(request):
    if request.method == "POST":
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('/laboratorio/')
        messages.error(request, "Falha no cadastro do usuário.")
    form = NovoUsuarioForm()
    context = {'form': form}
    return render(request, template_name='main/register.html', context=context)


def alterarSenha(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/laboratorio/')
        messages.error(request, "Falha na alteração da senha do usuário.")
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, template_name='main/alterar_senha.html', context=context)

"""
class UsuarioCreate(CreateView):
    template_name = "main/register.html"
    form_class = NovoUsuarioForm
    success_url = '/laboratorio/'
"""