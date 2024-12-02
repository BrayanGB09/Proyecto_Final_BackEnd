# Generated by Django 5.1.2 on 2024-11-21 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_propietario_propiedad_propietario_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='inquilino',
            new_name='cliente_id',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='propiedad',
            new_name='propiedad_id',
        ),
        migrations.CreateModel(
            name='ImagenPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='api.propiedad')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_detallada', models.TextField(blank=True, null=True)),
                ('propiedad', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='api.propiedad')),
                ('servicios', models.ManyToManyField(blank=True, related_name='detalles', to='api.servicio')),
                ('valoraciones', models.ManyToManyField(blank=True, related_name='detalles', to='api.valoracion')),
                ('imagenes', models.ManyToManyField(blank=True, related_name='detalles', to='api.imagenpropiedad')),
            ],
        ),
    ]
