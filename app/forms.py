# app/forms.py
from django import forms
from .models import Emocao

class RegistroEmocaoForm(forms.ModelForm):
    class Meta:
        model = Emocao
        fields = ['nome', 'data', 'intensidade']
