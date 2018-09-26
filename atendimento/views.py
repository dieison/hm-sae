from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})


def novo_paciente(request):
    form = PacienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'formulario_paciente.html', {'form': form})


def alterar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, instance=paciente)

    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')

    return render(request, 'formulario_paciente.html', {'form': form})

def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, instance=paciente)

    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'confirmar_excluir_paciente.html', {'paciente': paciente})
