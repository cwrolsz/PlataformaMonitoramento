from django.db import models
from django.contrib.auth.models import User

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


class RegistroEmocao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    intensidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

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
    id_personalizacao= models.AutoField(primary_key=True)
    Nome = models.ForeignKey(User, on_delete=models.CASCADE)
    Email = models.CharField(max_length=100)
    Senha = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Nome.username} - Personalização"


class SugestaoAtividades(models.Model):
    id_atividade = models.CharField(max_length=100, verbose_name="id da atividade")
    nome_atividade = models.CharField(max_length=100, verbose_name="nome da atividade")
    descricao = models.CharField(max_length=100, verbose_name="descrição")
    beneficios_emocionais = models.CharField(max_length=100, verbose_name="beneficios emocionais das atividades")

    def __str__(self):
        return f"{self.id_atividade}, {self.nome_atividade}, {self.descricao}, {self.beneficios_emocionais}"
    
    class Meta:
        verbose_name = "Sugestção de atividade"
        verbose_name_plural = "Sugestões de atividades"

class CompartilhamentoProgresso(models.Model):
    link = models.URLField(max_length=200)  # Campo para armazenar o link

    def __str__(self):
        return self.link