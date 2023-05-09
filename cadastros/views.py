from .models import Empresa, Categoria, Subcategoria, Promocao, Produto, Venda
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class EmpresaCreate(CreateView, LoginRequiredMixin):
    model = Empresa
    fields = ["nome", "email", "telefone", "documento", "endereco"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Empresa"
        return dados


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Categoria"
        return dados


class SubcategoriaCreate(CreateView):
    model = Subcategoria
    fields = ["nome_subcategoria",
              "descricao_subcategoria", "categoria_principal"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-subcategoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Subcategoria"
        return dados


class PromocaoCreate(CreateView):
    model = Promocao
    fields = ["titulo_promocao", "data_inicio", "data_fim", "descricao", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-promocao")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Promoção"
        return dados


class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome_produto", "descricao", "preco", "subcategoria"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Produtos"
        return dados


class VendaCreate(CreateView):
    model = Venda
    fields = ["nome_cliente", "endereco_montagem", "promocao",
              "telefone_cliente", "data_venda", "total", "data_pagamento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-venda")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Vendas"
        return dados


class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ["nome", "email", "telefone", "documento", "endereco"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-empresa")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Empresa"
        return dados


class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-categoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Categoria"
        return dados


class SubcategoriaUpdate(UpdateView):
    model = Subcategoria
    fields = ["nome_subcategoria",
              "descricao_subcategoria", "categoria_principal"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-subcategoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Subcategoria"
        return dados


class PromocaoUpdate(UpdateView):
    model = Promocao
    fields = ["titulo_promocao", "data_inicio",
              "data_fim", "descricao", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-promocao")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Promoção"
        return dados


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ["nome_produto", "descricao", "preco", "subcategoria"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Produto"
        return dados


class VendaUpdate(UpdateView):
    model = Venda
    fields = ["nome_cliente", "endereco_montagem", "pegue_monte", "promocao",
              "telefone_cliente", "data_venda", "total", "pago", "data_pagamento"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-venda")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Venda"
        return dados


#########################################################################################################


class EmpresaDelete(DeleteView):
    model = Empresa
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-empresa")


class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-categoria")


class SubcategoriaDelete(DeleteView):
    model = Subcategoria
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-subcategoria")


class PromocaoDelete(DeleteView):
    model = Promocao
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-promocao")


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-produto")


class VendaDelete(DeleteView):
    model = Venda
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-venda")


##################################################


class EmpresaList(ListView):
    model = Empresa
    template_name = "cadastros/list/empresa.html"


class CategoriaList(ListView):
    model = Categoria
    template_name = "cadastros/list/categoria.html"


class SubcategoriaList(ListView):
    model = Subcategoria
    template_name = "cadastros/list/subcategoria.html"


class PromocaoList(ListView):
    model = Promocao
    template_name = "cadastros/list/promocao.html"


class ProdutoList(ListView):
    model = Produto
    template_name = "cadastros/list/produto.html"


class VendaList(ListView):
    model = Venda
    template_name = "cadastros/list/venda.html"

##################################################


class EmpresaDetail(DetailView):
    model = Empresa
    template_name = "cadastros/detail/empresa.html"


class CategoriaDetail(DetailView):
    model = Categoria
    template_name = "cadastros/detail/categoria.html"


class SubcategoriaDetail(DetailView):
    model = Subcategoria
    template_name = "cadastros/detail/subcategoria.html"


class PromocaoDetail(DetailView):
    model = Promocao
    template_name = "cadastros/detail/promocao.html"


class ProdutoDetail(DetailView):
    model = Produto
    template_name = "cadastros/detail/produto.html"


class VendaDetail(DetailView):
    model = Venda
    template_name = "cadastros/detail/venda.html"


##################################################
