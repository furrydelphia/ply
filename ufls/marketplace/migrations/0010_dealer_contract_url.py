# Generated by Django 4.0.4 on 2023-03-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_dealer_table_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='contract_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
