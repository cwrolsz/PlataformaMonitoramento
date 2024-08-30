from django.contrib import admin
from .models import RegistroEmocao, AnalisePadroesEmocionais, IntegracaoDiarioPessoal, Personalizacao, SugestaoAtividades, CompartilhamentoProgresso

admin.site.register(RegistroEmocao)
admin.site.register(AnalisePadroesEmocionais)
admin.site.register(IntegracaoDiarioPessoal)
admin.site.register(Personalizacao)
admin.site.register(SugestaoAtividades)
admin.site.register(CompartilhamentoProgresso)  # Corrija o nome aqui
class EmocaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data', 'intensidade')