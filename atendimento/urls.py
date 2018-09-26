from django.urls import path

from .views import lista_pacientes
from .views import novo_paciente
from .views import alterar_paciente
from .views import excluir_paciente

urlpatterns = [
    path('lista/', lista_pacientes, name='lista_pacientes'),
    path('novo/', novo_paciente, name='novo_paciente'),
    path('alterar/<int:id>/', alterar_paciente, name='alterar_paciente'),
    path('excluir/<int:id>/', excluir_paciente, name='excluir_paciente'),
]
