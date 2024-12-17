from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from .models import Empresa, Categoria, Subcategoria, Promocao, Produto, Venda, MovimentoEstoque
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .filters import EmpresaFilter, CategoriaFilter, SubcategoriaFilter, PromocaoFilter, ProdutoFilter, VendaFilter


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render


from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Empresa

class EmpresaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()

    def handle_no_permission(self):
        return redirect('login')



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
    
    def get_queryset(self):
        return Subcategoria.objects.select_related("categoria_principal")


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
    fields = ["nome_produto", "descricao", "preco", "subcategoria", "quantidade_estoque"]
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
    
    def get_queryset(self):
        return Produto.objects.select_related("subcategoria")


class VendaCreate(CreateView, LoginRequiredMixin):
    model = Venda
    fields = ["nome_cliente", "endereco_montagem", "promocao", "telefone_cliente", "data_venda",
               "total", "data_pagamento", "pago", "pegue_monte", "produto", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-venda")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Vendas"
        return dados

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        form.instance.alterado_por = self.request.user
        # Salva a venda
        venda = form.save()

        # Lógica para atualizar o estoque e criar o movimento de estoque
        produto = venda.produto
        quantidade = venda.quantidade

        if produto.quantidade_estoque < quantidade:
            # Se o estoque não for suficiente, lança um erro
            form.add_error('quantidade', 'Estoque insuficiente para esta venda.')
            return self.form_invalid(form)

        # Cria um movimento de estoque (Saída, pois é uma venda)
        MovimentoEstoque.objects.create(
            produto=produto,
            tipo_movimento=MovimentoEstoque.SAIDA,
            quantidade_movimentada=quantidade,
            descricao=f"Venda para {venda.nome_cliente}"
        )

        # Atualiza o estoque do produto
        produto.quantidade_estoque -= quantidade
        produto.save()

        return super().form_valid(form)

    
    def get_queryset(self):
        return Venda.objects.select_related("promocao")
    





#########################################################################################################################


class EmpresaUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
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
    
    def get_queryset(self):
        self.object_list = Empresa.objects.filter(cadastrado_por=self.request.user)
        return self.object_list

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()

    def handle_no_permission(self):
        return redirect('login')
    


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
    
    def get_queryset(self):
        self.object_list = Promocao.objects.filter(cadastrado_por=self.request.user)
        return self.object_list



class ProdutoUpdate(UpdateView, LoginRequiredMixin):
    model = Produto
    fields = ["nome_produto", "descricao", "preco", "subcategoria", "quantidade_estoque"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-produto")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Produto"
        return dados
    
    def form_valid(self, form):
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)


class VendaUpdate(UpdateView, LoginRequiredMixin):
    model = Venda
    fields = ["nome_cliente", "endereco_montagem", "pegue_monte", "promocao", "telefone_cliente",
               "data_venda", "total", "pago", "data_pagamento" "produto", "quantidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-venda")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Alterar Venda"
        return dados
    
    def form_valid(self, form):
        form.instance.alterado_por = self.request.user
        return super().form_valid(form)
    

#########################################################################################################


class EmpresaDelete(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Empresa
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-empresa")

    def get_queryset(self):
        self.object_list = Empresa.objects.filter(cadastrado_por=self.request.user)
        return self.object_list

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()

    def handle_no_permission(self):
        return redirect('login')


class CategoriaDelete(DeleteView, LoginRequiredMixin):
    model = Categoria
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-categoria")



class SubcategoriaDelete(DeleteView, LoginRequiredMixin):
    model = Subcategoria
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-subcategoria")



class PromocaoDelete(DeleteView, LoginRequiredMixin):
    model = Promocao
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-promocao")

    def get_queryset(self):
        self.object_list = Promocao.objects.filter(cadastrado_por=self.request.user)
        return self.object_list



class ProdutoDelete(DeleteView, LoginRequiredMixin):
    model = Produto
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-produto")




class VendaDelete(DeleteView, LoginRequiredMixin):
    model = Venda
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-venda")




##################################################


class EmpresaList(FilterView, LoginRequiredMixin, UserPassesTestMixin):
    model = Empresa
    template_name = "cadastros/list/empresa.html"
    context_object_name = 'object_list'
    filterset_class = EmpresaFilter

    def get_queryset(self):
        self.object_list = Empresa.objects.filter(cadastrado_por=self.request.user)
        return self.object_list
    
    def get_queryset(self):
        self.object_list = Empresa.objects.filter(cadastrado_por=self.request.user)
        return self.object_list

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()

    def handle_no_permission(self):
        return redirect('login')


class CategoriaList(FilterView, LoginRequiredMixin):
    model = Categoria
    template_name = "cadastros/list/categoria.html"
    context_object_name = 'object_list'
    filterset_class = CategoriaFilter


class SubcategoriaList(FilterView, LoginRequiredMixin):
    model = Subcategoria
    template_name = "cadastros/list/subcategoria.html"
    context_object_name = 'object_list'
    filterset_class =SubcategoriaFilter

    def get_queryset(self):
        return Subcategoria.objects.select_related("categoria_principal")


class PromocaoList(FilterView, LoginRequiredMixin):
    model = Promocao
    template_name = "cadastros/list/promocao.html"
    context_object_name = 'object_list'
    filterset_class = PromocaoFilter

    def get_queryset(self):
        self.object_list = Promocao.objects.filter(cadastrado_por=self.request.user)
        return self.object_list

    def get_queryset(self):
        self.object_list = Promocao.objects.filter(cadastrado_por=self.request.user)
        return self.object_list


class ProdutoList(FilterView, LoginRequiredMixin):
    model = Produto
    template_name = "cadastros/list/produto.html"
    context_object_name = 'object_list'
    filterset_class = ProdutoFilter

    def get_queryset(self):
        return Produto.objects.select_related("subcategoria")


class VendaList(FilterView, LoginRequiredMixin):
    model = Venda
    template_name = "cadastros/list/venda.html"
    context_object_name = 'object_list'
    filterset_class = VendaFilter

    def get_queryset(self):
        return Venda.objects.select_related("promocao")

##################################################


class EmpresaDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Empresa
    template_name = "cadastros/detail/empresa.html"

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()

    def handle_no_permission(self):
        return redirect('login')


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

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()


    def handle_no_permission(self):
        return redirect('login')


class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = "cadastros/list/usuario.html"
    context_object_name = "usuarios"

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()

    def handle_no_permission(self):
        return redirect('login')
    

class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = "cadastros/form.html"
    fields = ["username", "first_name", "last_name", "email"]
    success_url = reverse_lazy("listar-usuarios")

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()

    def handle_no_permission(self):
        return redirect('login')
    

class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-usuarios")

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='admin').exists()

    def handle_no_permission(self):
        return redirect('login')


def home(request):
    produtos = Produto.objects.select_related("subcategoria").order_by('-data_inclusao')[:5]
    categorias = Categoria.objects.order_by('-nome')[:5]
    subcategorias = Subcategoria.objects.select_related("categoria_principal").order_by('-nome_subcategoria')[:5]
    promocoes = Promocao.objects.order_by('-data_inicio')[:5]
    vendas = Venda.objects.select_related("promocao").order_by('-data_venda')[:5]

    return render(request, 'cadastros/list/home.html', {
        'produtos': produtos,
        'categorias': categorias,
        'subcategorias': subcategorias,
        'promocoes': promocoes,
        'vendas': vendas,
    })
