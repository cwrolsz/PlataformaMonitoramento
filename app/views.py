from django.shortcuts import render, redirect
from .forms import RegistroEmocaoForm
from .models import RegistroEmocao, AnalisePadroesEmocionais, IntegracaoDiarioPessoal, Personalizacao, SugestaoAtividades, CompartilhamentoProgresso
from .models import Emocao

def criar_registro_emocao(request):
    if request.method == 'POST':
        form = RegistroEmocaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_registros_emocao')
    else:
        form = RegistroEmocaoForm()
    return render(request, 'criar_registro_emocao.html', {'form': form})


def listar_registros_emocao(request):
    registros = RegistroEmocao.objects.all()
    return render(request, 'listar_registros_emocao.html', {'registros': registros})

def criar_emocao(request):
    if request.method == 'POST':
        form = RegistroEmocaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_emocoes')  # Redireciona para a página de listagem após salvar
    else:
        form = RegistroEmocaoForm()
    return render(request, 'criar_registro_emocao.html', {'form': form})

def listar_emocoes(request):
    emocoes = Emocao.objects.all()
    return render(request, 'registro_emoções.html', {'emocoes': emocoes})

def analise_padroes_emocionais(request):
    padroes = AnalisePadroesEmocionais.objects.all()
    return render(request, 'analise_padroes_emocionais.html', {'padroes': padroes})


def integracao_diario_pessoal(request):
    integracoes = IntegracaoDiarioPessoal.objects.all()
    return render(request, 'integracao_diario_pessoal.html', {'integracoes': integracoes})


def personalizacao(request):
    personalizacoes = Personalizacao.objects.all()
    return render(request, 'personalizacao.html', {'personalizacoes': personalizacoes})


def sugestao_atividades(request):
    sugestoes = SugestaoAtividades.objects.all()
    return render(request, 'sugestao_atividades.html', {'sugestoes': sugestoes})


def compartilhamento_progresso(request):
    compartilhamentos = CompartilhamentoProgresso.objects.all()
    return render(request, 'compartilhamento_progresso.html', {'compartilhamentos': compartilhamentos})

def home(request):
    return render(request, 'home.html')
