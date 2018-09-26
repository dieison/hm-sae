from django.urls import path

from .views import lista_pacientes
from .views import novo_paciente

urlpatterns = [
    path('lista/', lista_pacientes, name='lista_pacientes'),
    path('novo/', novo_paciente, name='novo_paciente'),
]
