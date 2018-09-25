from django.urls import path

from .views import lista_pacientes

urlpatterns = [
    path('lista/', lista_pacientes),
]
