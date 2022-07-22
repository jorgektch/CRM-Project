from django.contrib import admin
from .models import CategoriaProducto, \
					Producto

# For images
from django.utils.html import format_html


@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "peso_en_kg", "stock")
    #list_display = ("nombre", "descripcion", "peso_en_kg", "stock", "imagen", "imagen_preview")
    #readonly_fields = ("imagen_preview",)
    """
    def image_tag(self,obj):
        return format_html('<img src="{0}" />'.format(obj.imagen.url))
    """
    """
    def imagen_preview(self, obj):
        return obj.imagen_preview
    imagen_preview.short_description = 'Imagen Preview'
    imagen_preview.allow_tags = True
    """