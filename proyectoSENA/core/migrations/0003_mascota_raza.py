# Generated by Django 3.1.6 on 2021-06-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_mascota_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.CharField(default='Criollo', max_length=30),
            preserve_default=False,
        ),
    ]
