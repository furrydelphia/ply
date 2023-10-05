# Generated by Django 4.0.4 on 2023-03-07 00:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0035_alter_application_closedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='closeDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 253663, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='application',
            name='openDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 253643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252852, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252836, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252826, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252882, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 0, 11, 29, 252754, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='webconnexaction',
            name='id',
            field=models.CharField(default=registration.models.StringKeyGenerator.__call__, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]
