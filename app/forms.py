from django import forms
from .models import RegistroEmocao

class RegistroEmocaoForm(forms.ModelForm):
    class Meta:
        model = RegistroEmocao
        fields = ['usuario', 'emocao', 'intensidade', 'descricao']
