# Generated by Django 3.2.4 on 2021-08-04 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_conbadgelevelmap_badgeimagelocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='printjob',
            name='handling',
            field=models.BooleanField(default=False),
        ),
    ]
