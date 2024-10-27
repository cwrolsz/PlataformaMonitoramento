from django.contrib import messages 
from .models import CompartilhamentoProgresso 
from django.shortcuts import render, redirect 
from .models import RegistroEmocao, AnalisePadroesEmocionais, IntegracaoDiarioPessoal, Personalizacao, SugestaoAtividades, CompartilhamentoProgresso
from .models import Emocao
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 
from .forms import RegistroEmocaoForm
from .models import RegistroEmocao


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages




from django.shortcuts import render, redirect, get_object_or_404
def criar_registro_emocao(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        emocao = request.POST['emocao']
        data = request.POST['data']
        intensidade = request.POST['intensidade']
        descricao = request.POST['descricao']

        novo_registro = RegistroEmocao(
            nome=nome,
            emocao=emocao,
            data=data,
            intensidade=intensidade,
            descricao=descricao
        )
        novo_registro.save()

        return redirect('listar_registros_emocao')

    return render(request, 'criar_registro_emocao.html')

# View para listar registros emocionais
def listar_registros_emocao(request):
    registros = RegistroEmocao.objects.all()
    return render(request, 'listar_registros_emocao.html', {'listar_registros_emocao': registros})

from django.shortcuts import get_object_or_404, redirect
from .models import RegistroEmocao

def excluir_registro(request, id):
    # Tenta obter o registro com o ID fornecido
    registro = get_object_or_404(RegistroEmocao, id=id)
    
    # Exclui o registro
    registro.delete()
    
    # Redireciona para uma página apropriada após a exclusão
    return redirect('listar_registros_emocao')  # ou qualquer outra URL que você desejar



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
    nome = request.session.get('nome', '')
    print(f'Nome do usuário: {nome}')  
    return render(request, 'home.html', {'nome': nome})

from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Feedback  # Certifique-se de que o modelo Feedback está importado

def feedback(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        Feedback.objects.create(descricao=descricao)  # Adiciona o feedback ao banco de dados
        return redirect('feedback')  # Redireciona para a mesma página após adicionar

    feedbacks = Feedback.objects.all()  # Recupera todos os feedbacks do banco de dados
    return render(request, 'feedback.html', {'feedbacks': feedbacks})
  # Substitua com o caminho correto do template

def meta(request):
    return render(request, 'meta.html')  # Substitua com o caminho correto do template

def estatisticas(request):
    return render(request, 'estatisticas.html')  # Substitua com o caminho correto do template

def lembretes(request):
    return render(request, 'lembretes.html')  # Substitua com o caminho correto do template




