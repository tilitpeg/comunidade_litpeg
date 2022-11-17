from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Laboratorio, Pessoa
from .forms import LaboratorioForm, PessoaForm, PessoaFormEdit
from django.db.models import Q
from django.core.paginator import Paginator


'''
Jeito anterior de listar os laboratórios
class ListaLaboratorioView(ListView):  
  model = Laboratorio
  queryset = Laboratorio.objects.all().order_by('nome_lab')

  def get_queryset(self):

    queryset = super().get_queryset()

    queryset = queryset.filter(usuario=self.request.user)

    filtro_nome = self.request.GET.get('nome') or None

    if filtro_nome:
      queryset = queryset.filter(nome_lab__contains=filtro_nome)
    
    return queryset
''' 
 
# Novo jeito com função que permite separar a aba de portaria
def laboratorio_List(request):
  
  if str(request.user) == str('portaria'):
    return redirect('pessoas.portaria')

  elif request.user.is_superuser:
    return redirect('laboratorio.admin')

  else:
  
    laboratorios = Laboratorio.objects.filter(usuario__username=request.user)
    
    search = request.GET.get('nome')
    
    if search:
      laboratorios = Laboratorio.objects.filter(
        Q(nome_lab__icontains=search) | Q(usuario__username__icontains=search)
        )

    return render(request, 'laboratorio/laboratorio_list.html', {'laboratorios': laboratorios})


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


def pessoas(request, pk_laboratorio=None):
  pessoas = Pessoa.objects.filter(laboratorio=pk_laboratorio, status = 'Ativo').order_by('nome_completo')
  
  paginator = Paginator(pessoas, 10)
  page = request.GET.get('page')
  pessoas = paginator.get_page(page)
  
  search = request.GET.get('search')

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
            pessoa.laboratorio_id = pk_laboratorio
            pessoa.save()
            return redirect(reverse('laboratorio.pessoas', args=[pk_laboratorio]))

    return render(request, 'pessoa/pessoa_form.html', {'form': form})


def pessoa_editar(request, pk_laboratorio, pk):
    '''print(pk_laboratorio)'''
    pessoa = get_object_or_404(Pessoa, pk=pk)
    form = PessoaFormEdit(instance=pessoa)
    if request.method == "POST":
        form = PessoaFormEdit(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect(reverse('laboratorio.pessoas', args=[pk_laboratorio]))
    print(pk_laboratorio)
    return render(request, 'pessoa/pessoa_form.html', {'form': form})


def pessoa_remover(request, pk_laboratorio, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
      pessoa.delete()
      return redirect(reverse('laboratorio.pessoas', args=[pk_laboratorio]))
    context = {
      "object": pessoa 
    }
    return render(request, 'pessoa/pessoa_confirm_delete.html', context)


#### Visualização do Admin e Portaria ####

# Mostra todos os laboratórios para o admin
def laboratorio_admin(request):
  
  laboratorios = Laboratorio.objects.all().order_by('nome_lab')
  
  search = request.GET.get('nome')
  
  if search:
    laboratorios = Laboratorio.objects.filter(
      Q(nome_lab__icontains=search) | Q(usuario__username__icontains=search)
      )

  return render(request, 'laboratorio/laboratorio_list_admin.html', {'laboratorios': laboratorios})


# Mostra todos os membros na aba "membros" para o admin
def pessoas_list_admin(request):
  search = request.GET.get('search')

  pessoas = Pessoa.objects.all().order_by('nome_completo')

  paginator = Paginator(pessoas, 10)
  page = request.GET.get('page')
  pessoas = paginator.get_page(page)
  
  if search:
    pessoas = Pessoa.objects.filter(
      Q(nome_completo__icontains=search) | Q(numero_cracha__icontains=search) | 
      Q(email__icontains=search) | Q(funcao__icontains=search) | Q(status__icontains=search)
      )

  return render(request, 'pessoa/pessoa_list_admin.html', {'pessoas': pessoas})


# Mostra todos os membros na aba "membros" para o admin, com uma navbar própria no html
def pessoas_list_portaria(request):
  search = request.GET.get('search')

  pessoas = Pessoa.objects.filter(status = 'Ativo').order_by('nome_completo')

  paginator = Paginator(pessoas, 10)
  page = request.GET.get('page')
  pessoas = paginator.get_page(page)
  
  if search:
    pessoas = Pessoa.objects.filter(
      Q(nome_completo__icontains=search) | Q(numero_cracha__icontains=search) | 
      Q(email__icontains=search) | Q(funcao__icontains=search) | Q(laboratorio__nome_lab__icontains=search)
      )

  return render(request, 'pessoa/pessoa_list_portaria.html', {'pessoas': pessoas})


# Edita a pessoa na aba membro do admin, sem a necessidade do pk_laboratorio
def pessoa_editar_admin(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    form = PessoaFormEdit(instance=pessoa)
    if request.method == "POST":
        form = PessoaFormEdit(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoas.admin')

    return render(request, 'pessoa/pessoa_form_admin.html', {'form': form})


# Remove a pessoa na aba membro do admin, sem a necessidade do pk_laboratorio
def pessoa_remover_admin(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
      pessoa.delete()
      return redirect('pessoas.admin')
    context = {
      "object": pessoa 
    }
    return render(request, 'pessoa/pessoa_confirm_delete_admin.html', context)