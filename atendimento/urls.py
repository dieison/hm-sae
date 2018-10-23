from django.urls import path

from .views import lista_pacientes
from .views import novo_paciente
from .views import alterar_paciente
from .views import excluir_paciente

from .views import lista_atendimentos
from .views import novo_atendimento
from .views import alterar_atendimento
from .views import excluir_atendimento


urlpatterns = [
    path('lista-pacientes/', lista_pacientes, name='lista_pacientes'),
    path('novo/', novo_paciente, name='novo_paciente'),
    path('alterar/<int:id>/', alterar_paciente, name='alterar_paciente'),
    path('excluir/<int:id>/', excluir_paciente, name='excluir_paciente'),

    path('lista-atendimentos/', lista_atendimentos, name='lista_atendimentos'),
    path('novo-atendimento/', novo_atendimento, name='novo_paciente'),
    path('alterar-atendimento/<int:id>/', alterar_atendimento, name='alterar_paciente'),
    path('excluir-atendimento/<int:id>/', excluir_atendimento, name='excluir_paciente'),
]
