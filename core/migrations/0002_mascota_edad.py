# Generated by Django 3.1.6 on 2021-06-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='edad',
            field=models.CharField(default='1 año', max_length=9),
            preserve_default=False,
        ),
    ]