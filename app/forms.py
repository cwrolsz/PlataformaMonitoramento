# app/forms.py
from django import forms # type: ignore
from .models import Emocao

class RegistroEmocaoForm(forms.ModelForm):
    class Meta:
        model = Emocao
        fields = ['nome', 'data', 'intensidade']
