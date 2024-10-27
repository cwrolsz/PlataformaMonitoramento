from django.contrib import admin
from django.urls import path
from app import views  # Certifique-se de importar as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('personalizacao/', views.personalizacao, name='personalizacao'),
    path('login/', views.personalizacao, name='login'),
    path('criar_registro_emocao/', views.criar_registro_emocao, name='criar_registro_emocao'),
    path('listar_registros_emocao/', views.listar_registros_emocao, name='listar_registros_emocao'),
    path('analise_padroes_emocionais/', views.analise_padroes_emocionais, name='analise_padroes_emocionais'),
    path('integracao_diario_pessoal/', views.integracao_diario_pessoal, name='integracao_diario_pessoal'),
    path('sugestao_atividades/', views.sugestao_atividades, name='sugestao_atividades'),
    path('compartilhamento_progresso/', views.compartilhamento_progresso, name='compartilhamento_progresso'),
    path('excluir/<int:id>/', views.excluir_registro, name='excluir_registro'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('meta/', views.meta, name='meta'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
    path('lembretes/', views.lembretes, name='lembretes'),
]
