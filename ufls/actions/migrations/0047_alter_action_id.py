# Generated by Django 4.2.4 on 2023-08-17 20:51

import actions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0046_alter_action_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='id',
            field=models.CharField(default=actions.models.StringKeyGenerator.__call__, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]