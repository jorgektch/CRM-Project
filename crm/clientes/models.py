from django.db import models

TipoDocumento_Opciones = (
    ('DNI','DNI'),
    ('CE', 'Carnet de extranjería'),
)

FuenteLead_Opciones = (
    ('Referencia personal', 'Referencia personal'),
    ('Sitio web', 'Sitio web de la empresa'),
    ('Facebook', 'Red social Facebook'),
    ('Instagram', 'Red social Instagram'),
    ('Twitter', 'Red social Twitter'),
    ('Youtube', 'Red social Youtube'),
)

class EstadoCliente(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    fecha_registro = models.DateField('Fecha de registro')
    fuente_lead = models.CharField(max_length=30, choices=FuenteLead_Opciones, default=None)
    
    tipo_documento = models.CharField(max_length=30, choices=TipoDocumento_Opciones, default='DNI')
    numero_documento = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

    ruc = models.CharField(max_length=200)
    razon_social = models.CharField(max_length=200)

    correo = models.CharField(max_length=200)
    celular = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    
    url_whatsapp = models.CharField(max_length=200)
    url_facebook = models.CharField(max_length=200)
    url_instagram = models.CharField(max_length=200)
    url_twitter = models.CharField(max_length=200)
    
    estado_cliente = models.ForeignKey(EstadoCliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido_paterno+" "+self.apellido_paterno+ ", "+self.nombre