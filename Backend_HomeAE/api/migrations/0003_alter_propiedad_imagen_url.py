# Generated by Django 5.1.2 on 2024-11-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_propiedad_imagen_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='imagen_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
