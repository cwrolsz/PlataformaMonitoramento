from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django import forms # type: ignore

class RegistroEmocao(models.Model):
    nome = models.CharField(max_length=100)    
    emocao = models.CharField(max_length=50)
    data = models.DateField()
    intensidade = models.CharField(max_length=10)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.emocao} - {self.intensidade}"


class RegistroEmocaoForm(forms.ModelForm):
    class Meta:
        model = RegistroEmocao
        fields = ['nome', 'emocao', 'data', 'intensidade', 'descricao']


class AnalisePadroesEmocionais(models.Model):
    id_relatorio = models.CharField(max_length=100, verbose_name="ID do relatório")
    id_usuario = models.CharField(max_length=100, verbose_name="ID do usuário")
    data_inicio = models.DateField(verbose_name="Data de início da análise")
    data_fim = models.DateField(verbose_name="Data de término da análise")
    resumo_emocional = models.TextField(verbose_name="Resumo emocional")

    def __str__(self):
        return f"{self.id_relatorio}, {self.id_usuario}, {self.data_inicio} - {self.data_fim}"

    class Meta:
        verbose_name = "Análise de Padrões Emocionais"


class Emocao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    intensidade = models.IntegerField()

    def __str__(self):
        return self.nome


class IntegracaoDiarioPessoal(models.Model):
    id_anotacao = models.CharField(max_length=100, verbose_name="ID da anotação")
    id_usuario = models.CharField(max_length=100, verbose_name="ID do usuário")
    data_hora = models.DateTimeField(verbose_name="Data e horário da integração no diário")
    texto_anotacao = models.TextField(verbose_name="Anotação no diário")

    def __str__(self):
        return f"{self.id_anotacao}, {self.id_usuario}, {self.data_hora}, {self.texto_anotacao}"

    class Meta:
        verbose_name = "Integração com o Diário pessoal"
        verbose_name_plural = "Integrações com o Diário pessoal"


class Personalizacao(models.Model):
    id_personalizacao = models.AutoField(primary_key=True)
    Nome = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    Senha = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.Nome.username}, {self.email}, {self.Senha} - Personalização"



class SugestaoAtividades(models.Model):
    id_atividade = models.CharField(max_length=100, verbose_name="id da atividade")
    nome_atividade = models.CharField(max_length=100, verbose_name="nome da atividade")
    descricao = models.CharField(max_length=100, verbose_name="descrição")
    beneficios_emocionais = models.CharField(max_length=100, verbose_name="benefícios emocionais das atividades")

    def __str__(self):
        return f"{self.id_atividade}, {self.nome_atividade}, {self.descricao}, {self.beneficios_emocionais}"

    class Meta:
        verbose_name = "Sugestão de atividade"
        verbose_name_plural = "Sugestões de atividades"


class CompartilhamentoProgresso(models.Model):
    link = models.CharField(max_length=255, default='seu_valor_padrao_aqui')

# models.py
from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data_feedback = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback de {self.usuario} - {self.data_feedback}'

class Meta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return f'Meta de {self.usuario} - {self.descricao}'

class Lembretes (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255)
    lida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Lembretes  para {self.usuario} - {self.mensagem}'

class Estatisticas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total_registros = models.IntegerField(default=0)
    total_feedbacks = models.IntegerField(default=0)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Estatísticas de {self.usuario} - Última atualização: {self.data_atualizacao}'

