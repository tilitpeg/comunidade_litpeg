from django import forms
from .models import Laboratorio, Pessoa

class LaboratorioForm(forms.ModelForm):
  class Meta:
    model = Laboratorio
    fields = ['nome_lab']


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'email', 'numero_cracha','funcao']