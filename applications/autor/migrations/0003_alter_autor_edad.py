# Generated by Django 3.2 on 2024-01-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_rename_nombre_autor_nombres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='edad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]