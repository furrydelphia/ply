# Generated by Django 4.2.4 on 2023-11-15 23:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationloot',
            name='stripe_price',
            field=models.TextField(max_length=200, verbose_name='Loot Stripe Price ID'),
        ),
        migrations.AlterField(
            model_name='registrationloot',
            name='stripe_price_test',
            field=models.TextField(max_length=200, verbose_name='Loot Stripe Test Price ID'),
        ),
        migrations.CreateModel(
            name='RegistrantLootFulfillment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Fulfilment Request ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Item Quantity')),
                ('active', models.BooleanField(default=False, verbose_name='Level Active')),
                ('fulfilled', models.BooleanField(default=False, verbose_name='Level Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Request Created')),
                ('fulfilled_on', models.DateTimeField(blank=True, null=True, verbose_name='Request Fulfilled on')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Request Remarks')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.event', verbose_name='Event')),
                ('loot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.registrationloot', verbose_name='Loot Type')),
                ('registrant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.registrant', verbose_name='Registrant')),
            ],
        ),
    ]
