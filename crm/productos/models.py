from django.db import models
# For image display
from django.utils.functional import cached_property
#from django.utils.html import format_html
from django.utils.html import mark_safe

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria_prodcuto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    peso_en_kg = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    #imagen = models.ImageField(null=True, blank=True, upload_to='productos/')
    #imagen = models.CharField(max_length=200) # models.ImageField(upload_to='productos')
    def __str__(self):
        return self.nombre
    """
    @property
    def imagen_preview(self):
        if self.imagen:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.imagen.url))
        return ""
    """
    """
    @cached_property
    def display_imagenxd(self):
        html = '<img src="{img}">'
        if self.imagenxd:
            return format_html(html, img=self.imagenxd.url)
        return format_html('<strong>There is no image for this entry.<strong>')
    display_imagenxd.short_description = 'Display image'
    """