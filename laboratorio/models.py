from django.db import models
from django.contrib.auth.models import User


class Laboratorio(models.Model):
  nome_lab = models.CharField(max_length=256, verbose_name='Nome do Laboratório')
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


  def __str__(self) -> str:
    return self.nome_lab


class Pessoa(models.Model):
  FUNCOES = [
    ('','Selecione sua função'),
    ("Docente", "Docente"),
    ("Discente","Discente"),
    ("Técnico", "Técnico"),
    ("Pesquisador", "Pesquisador"),
  ]

  nome_completo = models.CharField(max_length=256, verbose_name='Nome')
  email = models.EmailField(verbose_name='E-mail')
  numero_cracha = models.IntegerField(verbose_name='Número do Crachá')
  funcao = models.CharField(max_length=25, choices=FUNCOES, default='None', verbose_name='Função')
  laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
  sala = models.IntegerField(verbose_name='Sala', null=True, blank=True)
  ramal = models.IntegerField(verbose_name='Ramal', null=True, blank=True)

  def __str__(self) -> str:
    return self.nome_completo