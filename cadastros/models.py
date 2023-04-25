from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique = True)
    telefone = models.CharField(max_length=15)
    documento = models.CharField(max_length=18, help_text="CNPJ ou CPF")
    endereco = models.CharField(max_length=100, verbose_name="endereço")
    data_inclusao = models.DateTimeField(
        auto_now_add=True, verbose_name="data inclusão")
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
    data_inclusao = models.DateTimeField(auto_now_add=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(auto_now=True, verbose_name="data exclusão")

    def __str__(self):
        return f"{self.nome} ({self.descricao})"
    
    
class Subcategoria(models.Model):
    nome_subcategoria = models.CharField(max_length=50)
    descricao_subcategoria = models.CharField(max_length=100)
    categoria_principal = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    data_inclusao = models.DateTimeField(
        auto_now_add=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(
        auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(
        auto_now=True, verbose_name="data exclusão")

    def __str__(self):
        return f"{self.nome_subcategoria} ({self.descricao_subcategoria})"

class Promocao(models.Model):
    data_inclusao = models.DateTimeField(
        auto_now_add=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(
        auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(
        auto_now=True, verbose_name="data exclusão")
    ativo: models.BooleanField
    titulo_promocao: models.CharField(max_length=50, verbose_name="titulo promoção")
    data_inicio= models.DateTimeField()
    data_fim = models.DateTimeField()
    descricao: models.CharField(max_length=200, verbose_name="descrição")
    valor: models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"{self.titulo} ({self.descricao})"

    class Meta:
        verbose_name: "Promoção"

class Produto(models.Model):
    data_inclusao = models.DateTimeField(
        auto_now_add=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(
        auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(
        auto_now=True, verbose_name="data exclusão")
    ativo: models.BooleanField
    nome_produto: models.CharField(max_length=50)
    descricao: models.CharField(max_length=200, verbose_name="descrição")
    preco: models.DecimalField(decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome_produto} ({self.descricao})"
    
class Venda(models.Model):
    data_inclusao = models.DateTimeField(
        auto_now_add=True, verbose_name="data inclusão")
    data_alteracao = models.DateTimeField(
        auto_now=True, verbose_name="data alteração")
    data_exclusao = models.DateTimeField(
        auto_now=True, verbose_name="data exclusão")
    ativo: models.BooleanField
    nome_cliente: models.CharField(max_length=50)
    endereco_montagem: models.CharField(
        max_length=200, verbose_name="endereço montagem")
    pegue_monte: models.BooleanField
    telefone_cliente = models.CharField(max_length=15)
    data_venda = models.DateTimeField()
    total: models.DecimalField(decimal_places=2)
    pago: models.BooleanField
    data_pagamento = models.DateTimeField()
    promocao = models.ForeignKey(Promocao, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome_cliente} ({self.data_venda})"
