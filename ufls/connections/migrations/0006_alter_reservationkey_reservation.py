# Generated by Django 3.2.4 on 2022-03-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0005_auto_20220320_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationkey',
            name='reservation',
            field=models.JSONField(blank=True, default={}, null=True),
        ),
    ]
