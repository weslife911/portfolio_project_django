# Generated by Django 4.2.15 on 2024-11-10 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_adress_aboutuser_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='degree',
            old_name='degree',
            new_name='name',
        ),
    ]