from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Laboratorio, Pessoa
from .forms import LaboratorioForm, PessoaForm
from django.db.models import Q
from django.contrib.auth.models import User


class ListaLaboratorioView(ListView):
  model = Laboratorio
  queryset = Laboratorio.objects.all().order_by('nome_lab')

  def get_queryset(self):
    queryset = super().get_queryset()
    if str(self.request.user) != str('admin'):  # Mostra todos os Labs para o admin
      queryset = queryset.filter(usuario=self.request.user)

    filtro_nome = self.request.GET.get('nome') or None

    if filtro_nome:
      queryset = queryset.filter(nome_lab__contains=filtro_nome)
    
    return queryset


class LaboratorioCreateView(CreateView):
  model = Laboratorio
  form_class = LaboratorioForm
  success_url = '/laboratorio/'

  def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class LaboratorioUpdateView(UpdateView):
  model = Laboratorio
  form_class = LaboratorioForm
  success_url = '/laboratorio/'


class LaboratorioDeleteView(DeleteView):
  model = Laboratorio
  success_url = '/laboratorio/'


"""
# Outra opção de criar uma página propria para o admin e gerar os laboratórios
# Só precisando alterar as urls e o base.html
def laboratorio_admin(request, pk_laboratorio=None):
  search = request.GET.get('search')
  laboratorios = Laboratorio.objects.all().order_by('nome_lab')

  return render(request, 'laboratorio/laboratorio_list_admin.html', {'laboratorios': laboratorios})
"""


def pessoas(request, pk_laboratorio=None):
  search = request.GET.get('search')

  pessoas = Pessoa.objects.filter(laboratorio=pk_laboratorio)
  # Filtro Múltiplo (O "|" faz papel do "ou")
  if search:
    pessoas = Pessoa.objects.filter(Q(laboratorio=pk_laboratorio),  # Mostra somente os nomes vinculados ao laboratorio
      Q(nome_completo__icontains=search) | Q(numero_cracha__icontains=search) | 
      Q(email__icontains=search) | Q(funcao__icontains=search)
      )

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



