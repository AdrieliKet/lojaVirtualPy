from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique = True)
    telefone = models.CharField(max_length=15)
    documento = models.CharField(max_length=18, help_text="CNPJ ou CPF")
    endereco = models.CharField(max_length=100, verbose_name="endereço")
    data_inclusao = models.DateTimeField(
        auto_now=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(
        auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(
        auto_now=True, verbose_name="data exclusão")
    status = models.BooleanField

    def __str__(self):
        return f"{self.nome} ({self.documento})"


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100, verbose_name="descrição")
    data_inclusao = models.DateTimeField(auto_now=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(auto_now=True, verbose_name="data exclusão")

    def __str__(self):
        return f"{self.nome} ({self.descricao})"
    
    
class Subcategoria(models.Model):
    nome_subcategoria = models.CharField(max_length=50)
    descricao_subcategoria = models.CharField(max_length=100)
    categoria_principal = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    data_inclusao = models.DateTimeField(
        auto_now=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(
        auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(
        auto_now=True, verbose_name="data exclusão")

    def __str__(self):
        return f"{self.nome_subcategoria} ({self.descricao_subcategoria})"

class Usuario(models.Model):
    data_inclusao = models.DateTimeField(
        auto_now=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(
        auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(
        auto_now=True, verbose_name="data exclusão")
    ativo: models.BooleanField
    nome_usuario: models.CharField(max_length=50, verbose_name="nome usuário")
    sobrenome_usuario: models.CharField(
        max_length=50, verbose_name="sobrenome usuário")
    email: models.EmailField(max_length=100, unique=True)
    senha: models.CharField(max_length=10)
    empresa: Empresa
    data_ultimo_registro: models.DateTimeField(
        auto_now_add=True, verbose_name="data do último registro")

    def __str__(self):
        return f"{self.nome_usuario}"

    class Meta:
        verbose_name: "Usuário"
