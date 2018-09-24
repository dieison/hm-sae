from django.db import models
from datetime import datetime

class Paciente(models.Model):
    nome_do_Paciente = models.CharField(max_length=80)
    setor = models.CharField(max_length=30)
    leito = models.CharField(max_length=10)
    n_do_Prontuário = models.CharField(max_length=10)

    def __str__(self):
        return self.nome_do_Paciente

class Ficha(models.Model):

    paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)

    data = models.DateTimeField(default=datetime.now())

    #ConfortoNeurologico
    coma = models.BooleanField(default=False)
    nivel_de_conciência_diminuído = models.BooleanField(default=False, verbose_name='Nível deconciência diminuído')
    inquietação = models.BooleanField(default=False)
    agitação = models.BooleanField(default=False)
    alucinação = models.BooleanField(default=False)
    confusão = models.BooleanField(default=False)
    sonolência = models.BooleanField(default=False)

    # ConfortoCardiovascular
    FC_RC_ECG_alterados = models.BooleanField(default=False)
    alteração_PAS = models.BooleanField(default=False)
    FE_diminuída = models.BooleanField(default=False)
    fadiga = models.BooleanField(default=False)
    pulsos_pariféricos_diminuidos = models.BooleanField(default=False)
    pele_fria_úmida_pegajosa = models.BooleanField(default=False)
    distenção_da_veia_jugular = models.BooleanField(default=False)
    dispineia_paroxística_noturna = models.BooleanField(default=False)

    # Conforto respiratório
    alteração_no_padrão_respiratório = models.BooleanField(default=False)
    dispineia = models.BooleanField(default=False)
    cianose = models.BooleanField(default=False)
    SpO2_diminuída_PO2_diminuída = models.BooleanField(default=False)
    PCO2_aumentada = models.BooleanField(default=False)
    uso_da_musculatura_acessória = models.BooleanField(default=False)
    dificuldade_de_verbalização = models.BooleanField(default=False)
    sons_respiratórios_diminuídos_adventicos = models.BooleanField(default=False)
    escarro_em_exesso = models.BooleanField(default=False)
    tosse_ausente_ineficaz = models.BooleanField(default=False)
    VC_diminuído = models.BooleanField(default=False)
    respiração_descoordenada_em_relação_à_VM = models.BooleanField(default=False)
    derrame_pleural = models.BooleanField(default=False)

    # Conforto Gástrico
    alteração_no_paladar = models.BooleanField(default=False)
    diarreia = models.BooleanField(default=False)
    constipação = models.BooleanField(default=False)
    cólicas_dor_abdominal = models.BooleanField(default=False)
    sons_intestinais_hiperativos = models.BooleanField(default=False)
    fraqueza_dos_músculos_necessários_à_deglutição_mastigação = models.BooleanField(default=False)
    tônus_muscular_insuficiente = models.BooleanField(default=False)
    anorexia = models.BooleanField(default=False)
    ascite = models.BooleanField(default=False)

    # Conforto Urinário
    mucosas_secas = models.BooleanField(default=False)
    anúria_Olígúria = models.BooleanField(default=False)
    disúria = models.BooleanField(default=False)
    edema_ganho_de_peso = models.BooleanField(default=False)
    anasarca = models.BooleanField(default=False)
    perda_súbita_de_peso = models.BooleanField(default=False)
    sede_excessiva = models.BooleanField(default=False)
    desequilibrio_eletrolico = models.BooleanField(default=False)

    # Conforto Tegumentar
    extremos_de_idade = models.BooleanField(default=False)
    fator_mecânico = models.BooleanField(default=False)
    umidade = models.BooleanField(default=False)
    cor_anormal_da_pele = models.BooleanField(default=False)
    parestesia = models.BooleanField(default=False)
    pele_seca = models.BooleanField(default=False)
    alteração_na_integridade_da_pela = models.BooleanField(default=False)
    cicatrização_de_ferida_retardada = models.BooleanField(default=False)
    pulsos_periféricos_diminuídos_ou_ausentes = models.BooleanField(default=False)
    redução_na_amplitude_de_movimentos_ou_imobilidade_física = models.BooleanField(default=False)
    instabilidade_postural = models.BooleanField(default=False)
    hipertermia = models.BooleanField(default=False)
    hipotermia = models.BooleanField(default=False)

    # Conforto Psicológico
    apreenção = models.BooleanField(default=False)
    ansiedade = models.BooleanField(default=False)
    preocupação = models.BooleanField(default=False)
    desamparo = models.BooleanField(default=False)
    irritabilidade = models.BooleanField(default=False)
    nervosismo = models.BooleanField(default=False)
    tensão_ou_tensão_facial = models.BooleanField(default=False)
    dor = models.BooleanField(default=False)
    cooperação_diminuída = models.BooleanField(default=False)
    mudança_no_padrão_de_sono_ou_insonia = models.BooleanField(default=False)
    tremores = models.BooleanField(default=False)
    excitação_excessiva = models.BooleanField(default=False)
    aumento_da_transpiração = models.BooleanField(default=False)

    def __str__(self):
        return self.paciente.nome_do_Paciente
