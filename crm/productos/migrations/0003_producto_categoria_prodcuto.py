# Generated by Django 4.0.6 on 2022-07-22 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria_prodcuto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos.categoriaproducto'),
        ),
    ]
