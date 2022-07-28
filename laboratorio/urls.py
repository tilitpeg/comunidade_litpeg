from django.urls import path
from .views import ListaLaboratorioView, LaboratorioCreateView, LaboratorioUpdateView, LaboratorioDeleteView


urlpatterns = [
    path('', ListaLaboratorioView.as_view(), name='laboratorio.index'),
    path('novo/', LaboratorioCreateView.as_view(), name='laboratorio.novo'),
    path('editar/<int:pk>', LaboratorioUpdateView.as_view(), name='laboratorio.editar'),
    path('remover/<int:pk>', LaboratorioDeleteView.as_view(), name='laboratorio.remover'),

]