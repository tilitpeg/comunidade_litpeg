from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class NovoUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        nome = self.cleaned_data['username']
        nome = nome.lower()

        if User.objects.filter(username=nome).exists():
            raise ValidationError(f'Erro! O nome {nome} já está cadastrado.')
        
        return nome

    def clean_email(self):
      email_field = self.cleaned_data['email']
      email_field = email_field.lower()
      if User.objects.filter(email=email_field).exists():
        raise ValidationError(f'Erro! O email {email_field} já está cadastrado.')
      
      return email_field
    
    def save(self, commit=True):
        user = super(NovoUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
