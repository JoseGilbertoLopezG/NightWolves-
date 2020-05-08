# Generated by Django 3.0.5 on 2020-05-08 01:29

from django.db import migrations, models
import django.db.models.deletion
import food.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('descripcion', models.CharField(max_length=200, unique=True)),
                ('precio', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=food.models.direccion_imagenes_comida)),
            ],
        ),
        migrations.CreateModel(
            name='CantidadAlimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=5, validators=[food.models.numero])),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cantidad_alimento', to='food.Alimento')),
            ],
        ),
        migrations.CreateModel(
            name='CarritoDeCompras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=food.models.direccion_imagenes_comida)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=120, validators=[food.models.unique_name])),
            ],
        ),
        migrations.CreateModel(
            name='OrdenComida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(null=True, validators=[food.models.grade])),
                ('alimentos', models.ManyToManyField(related_name='articulos', through='food.CantidadAlimento', to='food.Alimento')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Cliente')),
                ('id_repartidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Repartidor')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Status')),
            ],
        ),
        migrations.AddField(
            model_name='cantidadalimento',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cantidad_alimento', to='food.OrdenComida'),
        ),
        migrations.AddField(
            model_name='alimento',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Categoria'),
        ),
    ]
