# Generated by Django 4.0.4 on 2022-08-18 23:18

import actions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0017_alter_action_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='id',
            field=models.CharField(default=actions.models.StringKeyGenerator.__call__, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]