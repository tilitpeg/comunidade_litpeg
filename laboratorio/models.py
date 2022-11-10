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
    ("Servidor Docente", "Servidor Docente"),
    ("Servidor Técnico","Servidor Técnico"),
    ("Técnico Terceirizado","Técnico Terceirizado"),
    ("Discente Graduação","Discente Graduação"),
    ("Discente Mestrado", "Discente Mestrado"),
    ("Discente Doutorado", "Discente Doutorado"),
    ("Discente Pós-Doutorado", "Discente Pós-Doutorado"),
    ("Outro", "Outro"),
  ]

  STATUS = [
    ("Ativo", "Ativo"),
    ("Inativo", "Inativo")
  ]

  GENERO = [
    ("", "Selecione uma opção"),
    ("Masculino", "Masculino"),
    ("Feminino", "Feminino"),
    ("Outro", "Outro"),
  ]

  BOLSISTA = [
    ("", "Selecione uma opção!"),
    ("Não", "Não"),
    ("Aluno Bolsista", "Aluno Bolsista"),
    ("Professor Bolsista (1A)", "Professor Bolsista (1A)"),
    ("Professor Bolsista (1B)", "Professor Bolsista (1B)"),
    ("Professor Bolsista (1C)", "Professor Bolsista (1C)"),
    ("Professor Bolsista (1D)", "Professor Bolsista (1D)"),
    ("Professor Bolsista (2)", "Professor Bolsista (2)"),
    ("Professor Bolsista (SR))", "Professor Bolsista (SR)"),
  ]

  nome_completo = models.CharField(max_length=256, verbose_name='Nome')
  email = models.EmailField(verbose_name='E-mail')
  genero = models.CharField(max_length=25, choices=GENERO, default='None', verbose_name='Gênero')
  numero_cracha = models.IntegerField(verbose_name='Número do Crachá')
  funcao = models.CharField(max_length=25, choices=FUNCOES, default='None', verbose_name='Função')
  bolsista = models.CharField(max_length=50, choices=BOLSISTA, default='None', verbose_name='É Bolsista?')
  laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
  sala = models.IntegerField(verbose_name='Sala', null=True, blank=True)
  ramal = models.IntegerField(verbose_name='Ramal', null=True, blank=True)
  status = models.CharField(max_length=25, choices=STATUS, default='Ativo', verbose_name='Status')


  def __str__(self) -> str:
    return self.nome_completo