# Generated by Django 3.2.15 on 2022-08-31 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos_socias', '0004_proyectos_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('icono', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='proyectos',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectos_socias.categorias'),
        ),
    ]
