# Generated by Django 5.1.2 on 2024-11-21 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_propiedad_valoracion_propiedad_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metodopago',
            old_name='usuario',
            new_name='usuario_id',
        ),
    ]
