from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Laboratorio
from .forms import LaboratorioForm


class ListaLaboratorioView(ListView):
  model = Laboratorio
  queryset = Laboratorio.objects.all().order_by('nome_lab')

  def get_queryset(self):
    queryset = super().get_queryset()
    filtro_nome = self.request.GET.get('nome') or None

    if filtro_nome:
      queryset = queryset.filter(nome_lab__contains=filtro_nome)
    
    return queryset


class LaboratorioCreateView(CreateView):
  model = Laboratorio
  form_class = LaboratorioForm
  success_url = '/laboratorio/'


class LaboratorioUpdateView(UpdateView):
  model = Laboratorio
  form_class = LaboratorioForm
  success_url = '/laboratorio/'


class LaboratorioDeleteView(DeleteView):
  model = Laboratorio
  success_url = '/laboratorio/'




