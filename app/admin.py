from django.contrib import admin
from .models import (
    RegistroEmocao, 
    AnalisePadroesEmocionais, 
    IntegracaoDiarioPessoal, 
    Personalizacao, 
    SugestaoAtividades, 
    CompartilhamentoProgresso,
    Feedback,
    Meta,
    Lembretes,
    Estatisticas
)

class EmocaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data', 'intensidade')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data_feedback')

class MetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'descricao', 'data_criacao', 'concluida')

class LembretesAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'mensagem', 'lida', 'data_criacao')

class EstatisticasAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'total_registros', 'total_feedbacks', 'data_atualizacao')

# Registrando modelos no painel de administração
admin.site.register(RegistroEmocao, EmocaoAdmin)
admin.site.register(AnalisePadroesEmocionais)
admin.site.register(IntegracaoDiarioPessoal)
admin.site.register(Personalizacao)
admin.site.register(SugestaoAtividades)
admin.site.register(CompartilhamentoProgresso)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Meta, MetaAdmin)
admin.site.register(Lembretes, LembretesAdmin)
admin.site.register(Estatisticas, EstatisticasAdmin)
