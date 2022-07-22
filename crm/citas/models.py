from django.db import models
from empleados.models import Empleado
from clientes.models import Cliente
from productos.models import Producto

class ModalidadCita(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)

	def __str__(self):
		return self.nombre

class AsuntoCita(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)

	def __str__(self):
		return self.nombre

class Cita(models.Model):
	asunto = models.ForeignKey(AsuntoCita, on_delete=models.CASCADE)
	modalidad = models.ForeignKey(ModalidadCita, on_delete=models.CASCADE, default=1)
	fecha_y_hora = models.DateTimeField('Fecha y hora')

	detalle = models.CharField(max_length=500)

	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	
	productos = models.ManyToManyField(Producto, related_name='productos')

	def __str__(self):
		return str(self.asunto)

