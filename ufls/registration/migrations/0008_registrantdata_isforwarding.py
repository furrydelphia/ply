# Generated by Django 3.2.4 on 2022-04-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20220128_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrantdata',
            name='isForwarding',
            field=models.BooleanField(default=False),
        ),
    ]
