# Generated by Django 5.1.2 on 2024-11-10 19:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_userskills_percentage_knowledge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskills',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
