# Generated by Django 3.1.6 on 2021-06-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0005_auto_20210618_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(default='N/A', max_length=1000, verbose_name='Descripción'),
            preserve_default=False,
        ),
    ]
