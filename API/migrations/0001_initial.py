# Generated by Django 4.2.1 on 2023-05-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('cedula', models.CharField(db_column='cedula', max_length=12, primary_key=True, serialize=False)),
                ('nombres', models.CharField(db_column='nombre', max_length=20)),
                ('apellidos', models.CharField(db_column='apellido', max_length=20)),
                ('email', models.EmailField(db_column='correo', max_length=254)),
                ('telefono1', models.CharField(db_column='telefono_opcional', max_length=25, null=True)),
            ],
        ),
    ]