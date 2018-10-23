from django.forms import ModelForm
from .models import Paciente
from .models import Ficha

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome_do_Paciente', 'setor', 'leito', 'n_do_Prontuário']

#class FichaForm(ModelForm):
#    class Meta:
#        model = Ficha
#        fields = ['nome_do_Paciente', 'setor', 'leito', 'n_do_Prontuário']
