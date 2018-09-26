from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})


def novo_paciente(request):
    form = PacienteForm(request.POST, None)

    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'formulario_paciente.html', {'form': form})
