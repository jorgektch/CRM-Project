from django.db import models

TipoDocumento_Opciones = (
	('DNI','DNI'),
	('CE', 'Carnet de extranjería'),
)

class CategoriaEmpleado(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)
	def __str__(self):
		return self.nombre

class Empleado(models.Model):
	tipo_documento = models.CharField(max_length=30, choices=TipoDocumento_Opciones, default='DNI')
	numero_documento = models.CharField(max_length=200)

	apellido_paterno = models.CharField(max_length=200)
	apellido_materno = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200)

	correo = models.CharField(max_length=200)
	celular = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)

	categoria_empleado = models.ForeignKey(CategoriaEmpleado, on_delete=models.CASCADE)
	def __str__(self):
		return self.apellido_paterno+" "+self.apellido_paterno+ ", "+self.nombre