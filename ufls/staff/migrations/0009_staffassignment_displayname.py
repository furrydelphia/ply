# Generated by Django 3.2.4 on 2022-07-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_alter_staffapplication_covidcert'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffassignment',
            name='displayName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
