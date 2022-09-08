# Generated by Django 3.2.15 on 2022-09-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos_socias', '0007_alter_categorias_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'verbose_name_plural': 'Categorías'},
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='Titulo',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='donativos',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='recaudo',
        ),
        migrations.AddField(
            model_name='proyectos',
            name='accionistas',
            field=models.IntegerField(default=1, help_text='Cantidad de accionisttas que tiene el proyecto'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='aportes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='camara_comercio',
            field=models.CharField(blank=True, help_text='Registro en camara de comercio', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='cedula',
            field=models.IntegerField(blank=True, help_text='Numero de cedula de la empresaria', null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='certificado_existencias',
            field=models.CharField(blank=True, help_text='texto de aiuda modificado', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='descripcion_integrantes',
            field=models.TextField(blank=True, help_text='Descripción de o los integrantes de la empresa o proyecto:\nNombre y apellido, mail, números de identificación, roles y HV\nen PDF de los integrantes del equipo.', null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='estatutos',
            field=models.CharField(blank=True, help_text='Montada del archivo a S3, convertir a binario y subir', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='fecha_creacion_empresa',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='fecha_creacion_socias',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='informacion',
            field=models.TextField(blank=True, help_text='- Volumen de ventas </br> - Datos de crecimiento </br> - Volumen de usuarios </br> - Plan de inversión </br> ', null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='monto_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='nit',
            field=models.IntegerField(blank=True, help_text='NIT de la empresa', null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='nombre',
            field=models.CharField(blank=True, help_text='Nombre del emprendimiento', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='producto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='rut',
            field=models.CharField(blank=True, help_text='Numero del Registro Unico Tributario (RUT)', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='video',
            field=models.CharField(blank=True, help_text='Link a YouTube con video explicativo de la empresa', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='icono',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='imagen',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='lugar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
