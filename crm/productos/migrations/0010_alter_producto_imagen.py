# Generated by Django 4.0.6 on 2022-07-22 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='#', upload_to='productos'),
        ),
    ]
