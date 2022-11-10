from django.contrib import admin
from .models import Laboratorio, Pessoa


class LaboratorioAdmin(admin.ModelAdmin):
  list_display = ('nome_lab', 'usuario')
  search_fields = ('nome_lab', 'usuario__username')
  # Quando houver uma foreignkeyfield é preciso colocar 'foreignkeyfield__field1'


class PessoaAdmin(admin.ModelAdmin):
  list_display = ('nome_completo', 'email', 'numero_cracha', 'funcao', 'laboratorio', 'sala', 'ramal', 'status')
  search_fields = ('nome_completo', 'email', 'numero_cracha', 'funcao', 'laboratorio__nome_lab', 'status')
  list_filter = ('laboratorio', 'status')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Pessoa, PessoaAdmin)
