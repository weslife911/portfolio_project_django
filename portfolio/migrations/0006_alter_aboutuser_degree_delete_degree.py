# Generated by Django 4.2.15 on 2024-11-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_rename_degree_degree_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuser',
            name='degree',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Degree',
        ),
    ]
