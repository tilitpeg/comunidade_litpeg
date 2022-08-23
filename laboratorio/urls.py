from django.urls import path
from .views import ListaLaboratorioView, LaboratorioCreateView, LaboratorioUpdateView, LaboratorioDeleteView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaLaboratorioView.as_view()), name='laboratorio.index'),
    path('laboratorio/', login_required(ListaLaboratorioView.as_view()), name='laboratorio.index'),
    path('adminlista/', login_required(views.laboratorio_admin), name='laboratorio.admin'),
    path('novo/', login_required(LaboratorioCreateView.as_view()), name='laboratorio.novo'),
    path('<int:pk>/editar', login_required(LaboratorioUpdateView.as_view()), name='laboratorio.editar'),
    path('<int:pk>/remover', login_required(LaboratorioDeleteView.as_view()), name='laboratorio.remover'),
    path('<int:pk_laboratorio>/pessoas', login_required(views.pessoas), name='laboratorio.pessoas'),
    path('adminpessoas/', login_required(views.pessoas_admin), name='laboratorio.pessoas.admin'),
    path('<int:pk_laboratorio>/pessoa/novo/', login_required(views.pessoa_novo), name='pessoa.novo'),
    path('<int:pk_laboratorio>/pessoa/<int:pk>/editar', login_required(views.pessoa_editar), name='pessoa.editar'),
    path('<int:pk_laboratorio>/pessoa/<int:pk>/remover', login_required(views.pessoa_remover), name='pessoa.remover'),

]