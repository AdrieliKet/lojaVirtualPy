from django.urls import path
from .views import EmpresaCreate, EmpresaUpdate, EmpresaList, EmpresaDetail, EmpresaDelete
from .views import CategoriaCreate, CategoriaUpdate, CategoriaList, CategoriaDetail, CategoriaDelete
from .views import SubcategoriaCreate, SubcategoriaUpdate, SubcategoriaList, SubcategoriaDetail, SubcategoriaDelete
from .views import PromocaoCreate, PromocaoUpdate, PromocaoList, PromocaoDetail, PromocaoDelete
from .views import ProdutoCreate, ProdutoUpdate, ProdutoList, ProdutoDetail, ProdutoDelete
from .views import VendaCreate, VendaUpdate, VendaList, VendaDetail, VendaDelete
from .views import UserRegisterView, UserListView, UserUpdateView, UserDeleteView
from .views import home

urlpatterns = [

    path("cadastrar/empresa/", EmpresaCreate.as_view(), name="cadastrar-empresa"),
    path("cadastrar/categoria/", CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("cadastrar/subcategoria/", SubcategoriaCreate.as_view(), name="cadastrar-subcategoria"),
    path("cadastrar/promocao/", PromocaoCreate.as_view(), name="cadastrar-promocao"),
    path("cadastrar/produto/", ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("cadastrar/venda/", VendaCreate.as_view(), name="cadastrar-venda"),


    path("editar/empresa/<int:pk>", EmpresaUpdate.as_view(), name="editar-empresa"),
    path("editar/categoria/<int:pk>", CategoriaUpdate.as_view(), name="editar-categoria"),
    path("editar/subcategoria/<int:pk>", SubcategoriaUpdate.as_view(), name="editar-subcategoria"),
    path("editar/promocao/<int:pk>", PromocaoUpdate.as_view(), name="editar-promocao"),
    path("editar/produto/<int:pk>", ProdutoUpdate.as_view(), name="editar-produto"),
    path("editar/venda/<int:pk>", VendaUpdate.as_view(), name="editar-venda"),


    path("excluir/empresa/<int:pk>/", EmpresaDelete.as_view(), name="excluir-empresa"),
    path("excluir/categoria/<int:pk>/", CategoriaDelete.as_view(), name="excluir-categoria"),
    path("excluir/subcategoria/<int:pk>/", SubcategoriaDelete.as_view(), name="excluir-subcategoria"),
    path("excluir/promocao/<int:pk>/", PromocaoDelete.as_view(), name="excluir-promocao"),
    path("excluir/produto/<int:pk>/", ProdutoDelete.as_view(), name="excluir-produto"),
    path("excluir/venda/<int:pk>/", VendaDelete.as_view(), name="excluir-venda"),


    path("listar/empresa/", EmpresaList.as_view(), name="listar-empresa"),
    path("listar/categoria/", CategoriaList.as_view(), name="listar-categoria"),
    path("listar/subcategoria/", SubcategoriaList.as_view(), name="listar-subcategoria"),
    path("listar/promocao/", PromocaoList.as_view(), name="listar-promocao"),
    path("listar/produto/", ProdutoList.as_view(), name="listar-produto"),
    path("listar/venda/", VendaList.as_view(),  name="listar-venda"),


    path("detalhar/empresa/<int:pk>/", EmpresaDetail.as_view(), name="detalhar-empresa"),
    path("detalhar/categoria/<int:pk>/", CategoriaDetail.as_view(), name="detalhar-categoria"),
    path("detalhar/subcategoria/<int:pk>/", SubcategoriaDetail.as_view(), name="detalhar-subcategoria"),
    path("detalhar/promocao/<int:pk>/",  PromocaoDetail.as_view(), name="detalhar-promocao"),
    path("detalhar/produto/<int:pk>/", ProdutoDetail.as_view(), name="detalhar-produto"),
    path("detalhar/venda/<int:pk>/", VendaDetail.as_view(), name="detalhar-venda"),

    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('usuarios/', UserListView.as_view(), name='listar-usuarios'),
    path('editar/usuario/<int:pk>/', UserUpdateView.as_view(), name='editar-usuario'),
    path('excluir/usuario/<int:pk>/', UserDeleteView.as_view(), name='excluir-usuario'),

    path('', home, name='home'),
]
