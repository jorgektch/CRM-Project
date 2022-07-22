from django.contrib import admin
from .models import CategoriaEmpleado, \
					Empleado

@admin.register(CategoriaEmpleado)
class CategoriaEmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("tipo_documento", "numero_documento", "apellido_paterno", "apellido_materno", "nombre", "categoria_empleado")
