from .models import Empresa, Categoria, Subcategoria, Usuario

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ["nome", "email", "telefone", "documento", "endereco"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ["nome", "email", "telefone", "documento", "endereco"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

# Create your views here.
