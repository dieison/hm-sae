from django.contrib import admin
from .models import Ficha, Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['n_do_Prontuário', 'nome_do_Paciente']
    search_fields = ['n_do_Prontuário', 'nome_do_Paciente']

class FichaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'data']
    search_fields = ['paciente', 'data']

admin.site.register(Ficha, FichaAdmin)
admin.site.register(Paciente, PacienteAdmin)
