# Generated by Django 3.2.4 on 2022-06-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_onboarding', '0004_alter_staffonboardrecord_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffonboardrecord',
            name='telegramHandle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
