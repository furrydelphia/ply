# Generated by Django 4.2.4 on 2023-08-17 20:42

import datetime
from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0049_alter_application_closedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='closeDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 368018, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='application',
            name='openDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 368014, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367794, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367791, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367788, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367785, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367801, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367798, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367770, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367781, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367776, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 20, 42, 58, 367759, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='webconnexaction',
            name='id',
            field=models.CharField(default=registration.models.StringKeyGenerator.__call__, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]
