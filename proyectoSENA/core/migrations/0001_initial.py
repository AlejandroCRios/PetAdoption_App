# Generated by Django 3.1.6 on 2021-06-11 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HogarPaso',
            fields=[
                ('idHogarPaso', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreRazon', models.CharField(max_length=50, verbose_name='Nombre/Razon Social')),
                ('tipoidentifica', models.CharField(choices=[('Cédula de ciudadanía', 'Cédula de ciudadanía'), ('NIT', 'NIT'), ('Pasaporte', 'Pasaporte'), ('Cédula de extranjería', 'Cédula de extranjería')], max_length=50, verbose_name='Tipo de indentificación')),
                ('numeroidentifica', models.CharField(max_length=50, verbose_name='Numero de identificación')),
                ('celular', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('correoE', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idMascota', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreMascota', models.CharField(max_length=30, verbose_name='Nombre mascota')),
                ('especieMascota', models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')], max_length=515)),
                ('tamanoMascota', models.CharField(choices=[('Grande', 'Grande'), ('Mediano', 'Mediano'), ('Pequeño', 'Pequeño')], max_length=15, verbose_name='Tamaño Mascota')),
                ('genero', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=15)),
                ('vacunacion', models.CharField(choices=[('Vacunado', 'Vacunado'), ('No vacunado', 'No vacunado')], max_length=15)),
                ('esterilizacion', models.CharField(choices=[('Esterilizado', 'Esterilizado'), ('No esterilizado', 'No esterilizado')], max_length=30)),
                ('imagen', models.ImageField(upload_to='Mascotas')),
                ('HogarPaso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hogarpaso')),
            ],
        ),
    ]
