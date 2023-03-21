from django.contrib import admin
from .models import Empresa, Categoria, Subcategoria

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
