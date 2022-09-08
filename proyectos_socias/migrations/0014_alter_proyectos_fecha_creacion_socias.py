# Generated by Django 3.2.15 on 2022-09-08 21:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos_socias', '0013_auto_20220908_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='fecha_creacion_socias',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 9, 8, 16, 35, 10, 848811), help_text='Fecha en la que creó el proyecto en Socias, por defecto', null=True),
        ),
    ]