# Generated by Django 4.0.4 on 2023-04-15 00:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_alter_application_closedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='closeDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='application',
            name='openDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92947, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='aaOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92698, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='dealersOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92690, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92711, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventsOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92707, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92677, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditClose',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92686, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regEditOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92682, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='regOpen',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 0, 1, 12, 92667, tzinfo=utc)),
        ),
    ]
