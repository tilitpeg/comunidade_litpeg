from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


def HomeView(request):
  return render(request, 'main/index.html')