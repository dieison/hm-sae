from django.forms import ModelForm
from .models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome_do_Paciente', 'setor', 'leito', 'n_do_Prontuário']
