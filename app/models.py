from django.db import models

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


from django.db import models

class RegistroEmocao(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    emocao = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    intensidade = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return f'{self.usuario} - {self.emocao} - {self.data}'


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
    id_usuario = models.CharField(max_length=100, verbose_name="ID do usuário")
    nome_usuario = models.CharField(max_length=100, verbose_name="Nome")
    idade = models.CharField(max_length=100, verbose_name="Idade")
    sexo = models.CharField(max_length=100, verbose_name="sexo")

    def __str__(self):
        return f"{self.id_usuario}, {self.nome_usuario}, {self.idade}, {self.sexo}"

    class Meta:
        verbose_name = "Personalização"


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

class CompartilhamentoProgresso(models.Model):  # Corrija o nome aqui
    progresso = models.TextField()
    data = models.DateField()

    def __str__(self):
        return f'Progresso: {self.progresso}'
