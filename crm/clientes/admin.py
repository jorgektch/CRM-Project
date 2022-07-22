from django.contrib import admin
from .models import EstadoCliente, \
					Cliente

@admin.register(EstadoCliente)
class EstadoClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("tipo_documento", "numero_documento", "apellido_paterno", "apellido_materno", "nombre", "estado_cliente")