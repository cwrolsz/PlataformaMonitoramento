from django.contrib import messages
from .models import CompartilhamentoProgresso 
from django.shortcuts import render, redirect
from .forms import RegistroEmocaoForm
from .models import RegistroEmocao, AnalisePadroesEmocionais, IntegracaoDiarioPessoal, Personalizacao, SugestaoAtividades, CompartilhamentoProgresso
from .models import Emocao
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render





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
    print("Função personalizacao chamada")  # Esta linha vai imprimir no console quando a função for chamada
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=name)
            if user.check_password(password):
                login(request, user)
                return redirect('pagina_inicial')  # Redirecione para a página inicial ou outra
            else:
                error = 'Nome de usuário ou senha inválidos.'
        except User.DoesNotExist:
            error = 'Nome de usuário ou senha inválidos.'

        return render(request, 'personalizacao.html', {'error': error})

    return render(request, 'personalizacao.html')


def sugestao_atividades(request):
    sugestoes = SugestaoAtividades.objects.all()
    return render(request, 'sugestao_atividades.html', {'sugestoes': sugestoes})

def compartilhamento_progresso(request):
    return render(request, 'compartilhamento_progresso.html')

def home(request):
    return render(request, 'home.html')
