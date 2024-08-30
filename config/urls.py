from django.contrib import admin
from django.urls import path
from app import views  # Certifique-se de importar as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Rota para a página inicial
    path('criar_registro_emocao/', views.criar_registro_emocao, name='criar_registro_emocao'),
    path('listar_registros_emocao/', views.listar_registros_emocao, name='listar_registros_emocao'),
    path('analise_padroes_emocionais/', views.analise_padroes_emocionais, name='analise_padroes_emocionais'),
    path('integracao_diario_pessoal/', views.integracao_diario_pessoal, name='integracao_diario_pessoal'),
    path('personalizacao/', views.personalizacao, name='personalizacao'),
    path('sugestao_atividades/', views.sugestao_atividades, name='sugestao_atividades'),
    path('compartilhamento_progresso/', views.compartilhamento_progresso, name='compartilhamento_progresso'),
    path('criar_registro_emocao/', views.criar_emocao, name='criar_registro_emocao'),
    path('registro_emoções/', views.listar_emocoes, name='listar_emocoes'),
]
