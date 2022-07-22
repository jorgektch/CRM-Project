from django.contrib import admin
from .models import ModalidadCita, \
					AsuntoCita, \
					Cita

@admin.register(ModalidadCita)
class ModalidadCitaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")

@admin.register(AsuntoCita)
class AsuntoCitaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("asunto", "modalidad", "fecha_y_hora", "detalle", "empleado", "cliente")