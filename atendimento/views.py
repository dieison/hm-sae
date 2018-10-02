from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import PacienteForm

@login_required
def lista_pacientes(request):
    termo_busca = request.GET.get('pesquisa', None)

    if termo_busca:
        pacientes = Paciente.objects.filter(nome_do_Paciente__icontains=termo_busca) | Paciente.objects.filter(n_do_Prontuário__icontains=termo_busca)
    else:
        pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})


@login_required
def novo_paciente(request):
    form = PacienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'formulario_paciente.html', {'form': form})


@login_required
def alterar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, instance=paciente)

    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')

    return render(request, 'formulario_paciente.html', {'form': form})


@login_required
def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)

    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'confirmar_excluir_paciente.html', {'paciente': paciente})
