from django.shortcuts import render
from .models import Paciente
# Create your views here.
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})
