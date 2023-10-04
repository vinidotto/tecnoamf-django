from django import forms
from .models import Estudante

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['first_name', 'last_name', 'email', 'foto', 'data_de_nascimento']
