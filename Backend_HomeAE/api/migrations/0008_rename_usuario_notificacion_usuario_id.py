# Generated by Django 5.1.2 on 2024-11-21 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_usuario_metodopago_usuario_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacion',
            old_name='usuario',
            new_name='usuario_id',
        ),
    ]
