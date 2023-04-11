from .models import Empresa, Categoria, Subcategoria, Promocao

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class EmpresaCreate(CreateView):
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
    fields = ["nome_subcategoria", "descricao_subcategoria", "categoria_principal"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-subcategoria")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Subcategoria"
        return dados
    

class PromocaoCreate(CreateView):
    model = Promocao
    fields = ["titulo_promocao", "data_inicio",
              "data_fim", "descricao", "valor"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-promocao")

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Promoção"
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
    fields = ["nome_subcategoria", "descricao_subcategoria", "categoria_principal"]
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
