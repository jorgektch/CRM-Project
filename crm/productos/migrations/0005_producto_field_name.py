# Generated by Django 4.0.6 on 2022-07-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_rename_peso_producto_peso_en_kg'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='field_name',
            field=models.ImageField(default='#', upload_to=None),
        ),
    ]