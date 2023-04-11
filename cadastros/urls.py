from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate
from .views import CategoriaCreate, CategoriaUpdate
from .views import SubcategoriaCreate, SubcategoriaUpdate
from .views import PromocaoCreate, PromocaoUpdate

urlpatterns = [

    path("cadastrar/empresa/", EmpresaCreate.as_view(), name="cadastrar-empresa"),
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/subcategoria/", SubcategoriaCreate.as_view(), name="cadastrar-subcategoria"),
    path("cadastrar/promocao/", PromocaoCreate.as_view(), name="cadastrar-promocao"),

    path("editar/empresa/<int:pk>", EmpresaUpdate.as_view(), name="editar-empresa"),
    path("editar/categoria/<int:pk>", CategoriaUpdate.as_view(), name="editar-categoria"),
    path("editar/subcategoria/<int:pk>", SubcategoriaUpdate.as_view(), name="editar-subcategoria"),
    path("editar/promocao/<int:pk>",
         PromocaoUpdate.as_view(), name="editar-promocao"),
]
