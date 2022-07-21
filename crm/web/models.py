from django.db import models

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)

class EstadoCliente(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)

class FuenteContacto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    celular = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    ruc = models.CharField(max_length=200)
    fecha_registro = models.DateField('Fecha de registro')
    fuente_contacto = models.ForeignKey(FuenteContacto, on_delete=models.CASCADE)
    estado_cliente = models.ForeignKey(EstadoCliente, on_delete=models.CASCADE)

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)

class Producto(models.Model):
    fuente_contacto = models.ForeignKey(FuenteContacto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    stock = models.IntegerField(default=0)
    imagen = models.CharField(max_length=200) # models.ImageField(upload_to='productos')

class CategoriaTrabajador(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)

class Trabajador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    celular = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    ruc = models.CharField(max_length=200)
    fecha_registro = models.DateField('Fecha de registro')
    categoria_trabajador = models.ForeignKey(CategoriaTrabajador, on_delete=models.CASCADE)

class Cita(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fechahora_agendada = models.DateTimeField('Fecha y hora agendada')