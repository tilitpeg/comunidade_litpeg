from django.urls import path
from .views import LaboratorioCreateView, LaboratorioUpdateView, LaboratorioDeleteView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.laboratorio_List), name='laboratorio.index'),
    path('laboratorio/', login_required(views.laboratorio_List), name='laboratorio.index'),
    path('adminlista/', login_required(views.laboratorio_admin), name='laboratorio.admin'),
    path('novo/', login_required(LaboratorioCreateView.as_view()), name='laboratorio.novo'),
    path('<int:pk>/editar', login_required(LaboratorioUpdateView.as_view()), name='laboratorio.editar'),
    path('<int:pk>/remover', login_required(LaboratorioDeleteView.as_view()), name='laboratorio.remover'),
    path('<int:pk_laboratorio>/pessoas', login_required(views.pessoas), name='laboratorio.pessoas'),
    path('adminpessoas/', login_required(views.pessoas_list_admin), name='laboratorio.pessoas.admin'),
    path('portariaPessoas/', login_required(views.pessoas_list_portaria), name='laboratorio.pessoas.portaria'),
    path('<int:pk_laboratorio>/pessoa/novo/', login_required(views.pessoa_novo), name='pessoa.novo'),
    path('<int:pk_laboratorio>/pessoa/<int:pk>/editar', login_required(views.pessoa_editar), name='pessoa.editar'),
    path('<int:pk_laboratorio>/pessoa/<int:pk>/remover', login_required(views.pessoa_remover), name='pessoa.remover'),

]