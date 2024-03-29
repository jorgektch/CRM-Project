# Generated by Django 4.0.6 on 2022-07-22 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_rename_peso_producto_peso_en_kg'),
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModalidadCita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='productos',
            field=models.ManyToManyField(related_name='productos', to='productos.producto'),
        ),
        migrations.AddField(
            model_name='cita',
            name='modalidad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='citas.modalidadcita'),
        ),
    ]
