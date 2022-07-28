from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Laboratorio, Pessoa
from .forms import LaboratorioForm, PessoaForm


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


def pessoas(request, pk_laboratorio):
  pessoas = Pessoa.objects.filter(laboratorio=pk_laboratorio)
  return render(request, 'pessoa/pessoa_list.html', {'pessoas': pessoas, 'pk_laboratorio': pk_laboratorio})


def pessoa_novo(request, pk_laboratorio):
    form = PessoaForm()
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.laboratorio_id = pk_laboratorio;
            pessoa.save()
            return redirect(reverse('laboratorio.pessoas', args=[pk_laboratorio]))

    return render(request, 'pessoa/pessoa_form.html', {'form': form})


def pessoa_editar(request, pk_laboratorio, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    form = PessoaForm(instance=pessoa)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect(reverse('laboratorio.pessoas', args=[pk_laboratorio]))

    return render(request, 'pessoa/pessoa_form.html', {'form': form})


def pessoa_remover(request, pk_laboratorio, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    pessoa.delete()
    return redirect(reverse('laboratorio.pessoas', args=[pk_laboratorio]))


