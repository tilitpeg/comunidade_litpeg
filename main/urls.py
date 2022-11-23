from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('register/', login_required(views.register), name='register'),
    path('alterarSenha/', login_required(views.alterarSenha), name='alterar.senha'),
    path('listamembro/', login_required(views.baixar_lista), name='baixar.lista'),
    path('estatisticas/', login_required(views.estatisticas), name='estatisticas'),
    path('total_func_ativo', login_required(views.total_func_ativo), name='total_func_ativo'),
    path('total_func_inativo', login_required(views.total_func_inativo), name='total_func_inativo'),
    path('divisao_genero', login_required(views.divisao_genero), name='divisao_genero'),
    path('divisao_bolsa', login_required(views.divisao_bolsa), name='divisao_bolsa'),
    path('divisao_funcao', login_required(views.divisao_funcao), name='divisao_funcao'),
    path('qtd_membros_por_lab', login_required(views.qtd_membros_por_lab), name='qtd_membros_por_lab'),

]