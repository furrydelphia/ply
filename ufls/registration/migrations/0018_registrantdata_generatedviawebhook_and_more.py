# Generated by Django 4.0.4 on 2022-08-14 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_webconnexaction_alter_application_closedate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrantdata',
            name='generatedViaWebhook',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='closeDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184738, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='application',
            name='openDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184721, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaClose',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184062, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaOpen',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184051, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersClose',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184039, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersOpen',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184027, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsClose',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184085, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsOpen',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184073, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regClose',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 183989, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditClose',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditOpen',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 184003, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regOpen',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 20, 33, 27, 183957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='webconnexaction',
            name='id',
            field=models.CharField(default=registration.models.StringKeyGenerator.__call__, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]