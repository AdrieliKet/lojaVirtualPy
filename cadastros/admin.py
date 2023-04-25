from django.contrib import admin
from .models import Empresa, Categoria, Subcategoria, Promocao, Produto, Venda

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Promocao)
admin.site.register(Produto)
admin.site.register(Venda)
