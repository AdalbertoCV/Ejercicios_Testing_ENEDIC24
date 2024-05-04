from django import forms
from .models import Partido, Candidato, Votacion

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['nombre', 'descripcion']

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'partido']

class VotacionForm(forms.ModelForm):
    class Meta:
        model = Votacion
        fields = ['candidato']  

    def __init__(self, *args, **kwargs):
        super(VotacionForm, self).__init__(*args, **kwargs)
        self.fields['candidato'].label_from_instance = lambda obj: f"{obj.nombre} {obj.apellido_paterno} {obj.apellido_materno}"
