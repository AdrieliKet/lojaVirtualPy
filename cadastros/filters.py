import django_filters
from .models import Empresa, Categoria, Subcategoria, Promocao, Produto, Venda

class EmpresaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='exact')
    telefone = django_filters.CharFilter(lookup_expr='icontains')
    documento = django_filters.CharFilter(lookup_expr='icontains')
    endereco = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Empresa
        fields = ['nome', 'email', 'telefone', 'documento', 'endereco']


class CategoriaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    descricao = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']


class SubcategoriaFilter(django_filters.FilterSet):
    nome_subcategoria = django_filters.CharFilter(lookup_expr='icontains')
    descricao_subcategoria = django_filters.CharFilter(lookup_expr='icontains')
    categoria_principal = django_filters.CharFilter(field_name='categoria_principal__nome', lookup_expr='icontains')


    class Meta:
        model = Subcategoria
        fields = ['nome_subcategoria',
              'descricao_subcategoria', 'categoria_principal']
        

class PromocaoFilter(django_filters.FilterSet):
    titulo_promocao = django_filters.CharFilter(lookup_expr='icontains')
    descricao = django_filters.CharFilter(lookup_expr='icontains')
    valor = django_filters.CharFilter(lookup_expr='gte')

    class Meta:
        model = Promocao
        fields = ['titulo_promocao', 'descricao', 'valor']


class ProdutoFilter(django_filters.FilterSet):
    nome_produto = django_filters.CharFilter(lookup_expr='icontains')
    preco = django_filters.CharFilter(lookup_expr='gte')
    subcategoria = django_filters.CharFilter(field_name='subcategoria__nome_subcategoria', lookup_expr='icontains')

    class Meta:
        model = Produto
        fields = ['nome_produto', 'preco', 'subcategoria']


class VendaFilter(django_filters.FilterSet):
    nome_cliente = django_filters.CharFilter(lookup_expr='icontains')
    promocao = django_filters.CharFilter(field_name='promocao__titulo_promocao', lookup_expr='icontains')
    data_venda = django_filters.CharFilter(lookup_expr='lte')
    data_pagamento = django_filters.CharFilter(lookup_expr='gte')
    pago = django_filters.CharFilter(lookup_expr='exact')
    pegue_monte = django_filters.CharFilter(lookup_expr='exact')
    produto = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Venda
        fields =  ['nome_cliente', 'promocao', 'data_venda',
               'data_pagamento', 'pago', 'pegue_monte', 'produto',]