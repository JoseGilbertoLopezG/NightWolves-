# Generated by Django 3.0.3 on 2020-05-08 08:18

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nombre', models.CharField(max_length=80)),
                ('ap_paterno', models.CharField(max_length=110)),
                ('ap_materno', models.CharField(blank=True, max_length=110)),
                ('correo', models.EmailField(max_length=300, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20, validators=[users.models.numero_telefono])),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Repartidor'), (3, 'Cliente')])),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=60)),
                ('numero_lt', models.CharField(max_length=5)),
                ('numero_mz', models.CharField(max_length=5)),
                ('numero_interior', models.CharField(blank=True, max_length=5)),
                ('colonia', models.CharField(max_length=40)),
                ('delegacion', models.CharField(max_length=20)),
                ('cp', models.CharField(max_length=10)),
                ('direccion', models.ManyToManyField(related_name='usuario_asociado', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
