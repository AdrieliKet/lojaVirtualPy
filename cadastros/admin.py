from django.contrib import admin
from .models import Empresa, Categoria, Subcategoria, Promocao

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Promocao)
