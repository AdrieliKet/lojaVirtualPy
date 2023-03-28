from django.contrib import admin
from .models import Empresa, Categoria, Subcategoria, Usuario

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Usuario)
