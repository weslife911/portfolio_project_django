# Generated by Django 4.2.15 on 2024-11-10 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_aboutuser_experience_alter_aboutuser_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutuser',
            old_name='adress',
            new_name='address',
        ),
    ]
