from django.contrib import admin
from .models import RegistroEmocao, AnalisePadroesEmocionais, IntegracaoDiarioPessoal, Personalizacao, SugestaoAtividades, CompartilhamentoProgresso

class EmocaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data', 'intensidade')

# Registrando modelos no painel de administração
admin.site.register(RegistroEmocao, EmocaoAdmin)
admin.site.register(AnalisePadroesEmocionais)
admin.site.register(IntegracaoDiarioPessoal)
admin.site.register(Personalizacao)
admin.site.register(SugestaoAtividades)
admin.site.register(CompartilhamentoProgresso)
