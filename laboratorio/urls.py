from django.urls import path
from .views import ListaLaboratorioView, LaboratorioCreateView, LaboratorioUpdateView, LaboratorioDeleteView
from . import views

urlpatterns = [
    path('', ListaLaboratorioView.as_view(), name='laboratorio.index'),
    path('novo/', LaboratorioCreateView.as_view(), name='laboratorio.novo'),
    path('<int:pk>/editar', LaboratorioUpdateView.as_view(), name='laboratorio.editar'),
    path('<int:pk>/remover', LaboratorioDeleteView.as_view(), name='laboratorio.remover'),
    path('<int:pk_laboratorio>/pessoas', views.pessoas, name='laboratorio.pessoas'),
    path('<int:pk_laboratorio>/pessoa/novo/', views.pessoa_novo, name='pessoa.novo'),
    path('<int:pk_laboratorio>/pessoa/<int:pk>/editar', views.pessoa_editar, name='pessoa.editar'),
    path('<int:pk_laboratorio>/pessoa/<int:pk>/remover', views.pessoa_remover, name='pessoa.remover'),

]