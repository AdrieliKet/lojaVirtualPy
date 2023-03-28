from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate
from .views import CategoriaCreate, CategoriaUpdate

urlpatterns = [

    path("cadastrar/empresa/", EmpresaCreate.as_view(), name="cadastrar-empresa"),
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),

    path("editar/empresa/<int:pk>", EmpresaUpdate.as_view(), name="editar-empresa"),
    path("editar/categoria/<int:pk>", CategoriaUpdate.as_view(), name="editar-categoria"),
]
