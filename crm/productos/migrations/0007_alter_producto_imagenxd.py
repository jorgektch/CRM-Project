# Generated by Django 4.0.6 on 2022-07-22 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_remove_producto_field_name_producto_imagenxd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenxd',
            field=models.ImageField(default='#', upload_to='productos'),
        ),
    ]
