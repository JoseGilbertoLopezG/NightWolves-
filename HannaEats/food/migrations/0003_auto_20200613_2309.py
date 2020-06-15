# Generated by Django 3.0.3 on 2020-06-13 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import food.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0002_auto_20200611_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='descripcion',
            field=models.CharField(error_messages={'max_length': 'La longitud máxima es de 200 caracteres', 'required': 'Este campo es obligatorio'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='nombre',
            field=models.CharField(error_messages={'max_length': 'La longitud máxima es de 120 caracteres', 'required': 'Este campo es obligatorio', 'unique': 'Un alimento con este nombre ya existe'}, max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='precio',
            field=models.FloatField(error_messages={'invalid': 'Tienes que proporcionar un número (puede tener decimales)', 'required': 'Este campo es obligatorio'}),
        ),
        migrations.AlterField(
            model_name='cantidadalimento',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(error_messages={'max_length': 'La longitud máxima es de 120 caracteres', 'required': 'Este campo es obligatorio', 'unique': 'Una categoria con este nombre ya existe'}, max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='ordencomida',
            name='alimentos',
            field=models.ManyToManyField(blank=True, related_name='articulos', through='food.CantidadAlimento', to='food.Alimento'),
        ),
        migrations.AlterField(
            model_name='ordencomida',
            name='calificacion',
            field=models.IntegerField(blank=True, null=True, validators=[food.models.grade]),
        ),
        migrations.AlterField(
            model_name='ordencomida',
            name='id_repartidor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='repartidor', to=settings.AUTH_USER_MODEL),
        ),
    ]