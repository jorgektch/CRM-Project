# Generated by Django 4.0.6 on 2022-07-22 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(choices=[('DNI', 'DNI'), ('CE', 'Carnet de extranjería')], default='DNI', max_length=30)),
                ('numero_documento', models.CharField(max_length=200)),
                ('apellido_paterno', models.CharField(max_length=200)),
                ('apellido_materno', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('categoria_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.categoriaempleado')),
            ],
        ),
    ]