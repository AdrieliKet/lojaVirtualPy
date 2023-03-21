from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    documento = models.CharField(max_length=18, help_text="CNPJ ou CPF")
    endereco = models.CharField(max_length=100)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    data_exclusao = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField

    def __str__(self):
        return f"{self.nome} ({self.documento})"
    

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.descricao})"
    
    
class Subcategoria(models.Model):
    nome_subcategoria = models.CharField(max_length=50)
    descricao_subcategoria = models.CharField(max_length=100)
    categoria_principal = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome_subcategoria} ({self.descricao_subcategoria})"
