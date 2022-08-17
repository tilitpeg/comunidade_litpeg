from django.contrib import admin
from .models import Laboratorio, Pessoa


class LaboratorioAdmin(admin.ModelAdmin):
  list_display = ('nome_lab', 'usuario')
  search_fields = ('nome_lab', 'usuario')


class PessoaAdmin(admin.ModelAdmin):
  list_display = ('nome_completo', 'email', 'numero_cracha', 'funcao', 'laboratorio')
  search_fields = ('nome_completo', 'email', 'numero_cracha', 'funcao', 'laboratorio')
  list_filter = ('laboratorio',)

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Pessoa, PessoaAdmin)
