from django.contrib import admin

from .models import TipoDocumento, \
					EstadoCliente, \
					FuenteContacto, \
					Cliente, \
					CategoriaProducto, \
					Producto, \
					CategoriaTrabajador, \
					Trabajador, \
					Cita

admin.site.register(TipoDocumento)
admin.site.register(EstadoCliente)
admin.site.register(FuenteContacto)
admin.site.register(Cliente)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(CategoriaTrabajador)
admin.site.register(Trabajador)
admin.site.register(Cita)