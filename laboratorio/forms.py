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
        fields = ['nome_completo', 'email', 'genero', 'numero_cracha','funcao', 'bolsista', 'sala', 'ramal', 'status']

    def clean_nome_completo(self):
      nome = self.cleaned_data['nome_completo']
      nome = nome.title()

      if Pessoa.objects.filter(nome_completo=nome).exists():
        raise ValidationError(f'Erro! O nome {nome} já está cadastrado.')
      
      return nome

    def clean_email(self):
      email_field = self.cleaned_data['email']
      email_field = email_field.lower()
      if Pessoa.objects.filter(email=email_field).exists():
        raise ValidationError(f'Erro! O email {email_field} já está cadastrado.')
      
      return email_field

    def clean_numero_cracha(self):
      numero_cracha_field = self.cleaned_data['numero_cracha']
      if Pessoa.objects.filter(numero_cracha=numero_cracha_field).exists():
        raise ValidationError(f'Erro! O crachá {numero_cracha_field} já está cadastrado.')
      
      return numero_cracha_field


# TESTE PARA DECIDIR FUTURAMENTE
# Serve para editar os membros atuais sem fazer o tratamento de repetição
# Mas ao mesmo tempo permite que na edição seja repetido algum campo.
# Só trocar o PessoaForm por PessoaFormEdit
class PessoaFormEdit(forms.ModelForm):
  class Meta:
      model = Pessoa
      fields = ['nome_completo', 'email', 'genero', 'numero_cracha','funcao', 'bolsista', 'sala', 'ramal', 'status']
