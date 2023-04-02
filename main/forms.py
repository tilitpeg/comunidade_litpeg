from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

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


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}), label='Login de Usuário')

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}), label='Senha')

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'class': 'form-control'}), label='Captcha')