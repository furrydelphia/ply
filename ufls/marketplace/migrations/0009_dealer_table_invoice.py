# Generated by Django 4.0.4 on 2023-03-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_dealer_upgr_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='table_invoice',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]