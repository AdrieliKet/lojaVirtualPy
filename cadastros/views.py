from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from .models import Empresa, Categoria, Subcategoria, Promocao, Produto, Venda
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class EmpresaCreate(CreateView, LoginRequiredMixin):
    model = Empresa
    fields = ["nome", "email", "telefone", "documento", "endereco"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Empresa"
        return dados

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)


class CategoriaCreate(CreateView, LoginRequiredMixin):
    model = Categoria
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Categoria"
        return dados

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)


class SubcategoriaCreate(CreateView, LoginRequiredMixin):
    model = Subcategoria
    fields = ["nome_subcategoria",
              "descricao_subcategoria", "categoria_principal"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-subcategoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Subcategoria"
        return dados

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)


class PromocaoCreate(CreateView, LoginRequiredMixin):
    model = Promocao
    fields = ["titulo_promocao", "data_inicio", "data_fim", "descricao", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-promocao")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Promoção"
        return dados

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)


class ProdutoCreate(CreateView, LoginRequiredMixin):
    model = Produto
    fields = ["nome_produto", "descricao", "preco", "subcategoria"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Produtos"
        return dados

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)


class VendaCreate(CreateView, LoginRequiredMixin):
    model = Venda
    fields = ["nome_cliente", "endereco_montagem", "promocao",
              "telefone_cliente", "data_venda", "total", "data_pagamento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-venda")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Vendas"
        return dados

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)

#########################################################################################################################


class EmpresaUpdate(UpdateView, LoginRequiredMixin):
    model = Empresa
    fields = ["nome", "email", "telefone", "documento", "endereco"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Empresa"
        return dados
    
    def form_valid(self, form):
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)
    
    def get_object(self):
        self.object = get_object_or_404(Empresa, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class CategoriaUpdate(UpdateView, LoginRequiredMixin):
    model = Categoria
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Categoria"
        return dados
    
    def form_valid(self, form):
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)
    
    def get_object(self):
        self.object = get_object_or_404(
            Categoria, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class SubcategoriaUpdate(UpdateView, LoginRequiredMixin):
    model = Subcategoria
    fields = ["nome_subcategoria",
              "descricao_subcategoria", "categoria_principal"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-subcategoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Subcategoria"
        return dados

    def form_valid(self, form):
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)
    
    def get_object(self):
        self.object = get_object_or_404(
            Subcategoria, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class PromocaoUpdate(UpdateView, LoginRequiredMixin):
    model = Promocao
    fields = ["titulo_promocao", "data_inicio",
              "data_fim", "descricao", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-promocao")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Promoção"
        return dados
    
    def form_valid(self, form):
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)

    def get_object(self):
        self.object = get_object_or_404(
            Promocao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class ProdutoUpdate(UpdateView, LoginRequiredMixin):
    model = Produto
    fields = ["nome_produto", "descricao", "preco", "subcategoria"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Produto"
        return dados
    
    def form_valid(self, form):
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)

    def get_object(self):
        self.object = get_object_or_404(Produto, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class VendaUpdate(UpdateView, LoginRequiredMixin):
    model = Venda
    fields = ["nome_cliente", "endereco_montagem", "pegue_monte", "promocao",
              "telefone_cliente", "data_venda", "total", "pago", "data_pagamento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-venda")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Venda"
        return dados
    
    def form_valid(self, form):
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)

    def get_object(self):
        self.object = get_object_or_404(Venda, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


#########################################################################################################


class EmpresaDelete(DeleteView, LoginRequiredMixin):
    model = Empresa
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-empresa")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Empresa, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class CategoriaDelete(DeleteView, LoginRequiredMixin):
    model = Categoria
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-categoria")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Categoria, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class SubcategoriaDelete(DeleteView, LoginRequiredMixin):
    model = Subcategoria
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-subcategoria")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Subcategoria, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class PromocaoDelete(DeleteView, LoginRequiredMixin):
    model = Promocao
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-promocao")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Promocao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class ProdutoDelete(DeleteView, LoginRequiredMixin):
    model = Produto
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-produto")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Produto, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class VendaDelete(DeleteView, LoginRequiredMixin):
    model = Venda
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-venda")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Venda, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


##################################################


class EmpresaList(ListView, LoginRequiredMixin):
    model = Empresa
    template_name = "cadastros/list/empresa.html"

    def get_queryset(self):
        self.object_list = Empresa.objects.filter(cadastrado_por=self.request.user)
        return self.object_list


class CategoriaList(ListView, LoginRequiredMixin):
    model = Categoria
    template_name = "cadastros/list/categoria.html"


class SubcategoriaList(ListView, LoginRequiredMixin):
    model = Subcategoria
    template_name = "cadastros/list/subcategoria.html"


class PromocaoList(ListView, LoginRequiredMixin):
    model = Promocao
    template_name = "cadastros/list/promocao.html"


class ProdutoList(ListView, LoginRequiredMixin):
    model = Produto
    template_name = "cadastros/list/produto.html"


class VendaList(ListView, LoginRequiredMixin):
    model = Venda
    template_name = "cadastros/list/venda.html"

##################################################


class EmpresaDetail(DetailView, LoginRequiredMixin):
    model = Empresa
    template_name = "cadastros/detail/empresa.html"


class CategoriaDetail(DetailView, LoginRequiredMixin):
    model = Categoria
    template_name = "cadastros/detail/categoria.html"


class SubcategoriaDetail(DetailView, LoginRequiredMixin):
    model = Subcategoria
    template_name = "cadastros/detail/subcategoria.html"


class PromocaoDetail(DetailView, LoginRequiredMixin):
    model = Promocao
    template_name = "cadastros/detail/promocao.html"


class ProdutoDetail(DetailView, LoginRequiredMixin):
    model = Produto
    template_name = "cadastros/detail/produto.html"


class VendaDetail(DetailView, LoginRequiredMixin):
    model = Venda
    template_name = "cadastros/detail/venda.html"


##################################################
