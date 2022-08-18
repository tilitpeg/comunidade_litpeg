import imp
from django import forms
from .models import Laboratorio, Pessoa
from django.core.exceptions import ValidationError


class LaboratorioForm(forms.ModelForm):
  class Meta:
    model = Laboratorio
    fields = ['nome_lab']

  def clean_nome_lab(self):
      nome = self.cleaned_data['nome_lab']
      if Laboratorio.objects.filter(nome_lab=nome).exists():
        raise ValidationError(f'Erro! O laboratório {nome} já está cadastrado.')
      
      return nome


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'email', 'numero_cracha','funcao']

    def clean_nome_completo(self):
      nome = self.cleaned_data['nome_completo']
      if Pessoa.objects.filter(nome_completo=nome).exists():
        raise ValidationError(f'Erro! O nome {nome} já está cadastrado.')
      
      return nome

    def clean_email(self):
      email_field = self.cleaned_data['email']
      if Pessoa.objects.filter(email=email_field).exists():
        raise ValidationError(f'Erro! O email {email_field} já está cadastrado.')
      
      return email_field