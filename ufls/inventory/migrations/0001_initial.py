# Generated by Django 3.2.4 on 2021-07-26 23:06

from django.db import migrations, models
import django.db.models.deletion
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('furry', '0007_auto_20210515_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('access_codes', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='furry.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('tag', models.CharField(default=inventory.models.genRandNum, max_length=5, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(choices=[('CP', 'Computer'), ('SV', 'Server'), ('CH', 'Chromebook'), ('AP', 'Access Point'), ('TB', 'Tablet'), ('CA', 'Card Printer'), ('PR', 'Traditional Printer'), ('SW', 'Networking Switch'), ('LO', 'Loaned Hardware'), ('BX', 'Box'), ('TO', 'Tote'), ('OT', 'Other')], max_length=2)),
                ('company', models.CharField(choices=[('FDL', 'Furrydelphia, Inc.')], default='FDL', max_length=3)),
                ('description', models.CharField(max_length=250)),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('is_convention_owned', models.BooleanField(default=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('checked_out_to', models.CharField(blank=True, max_length=100, null=True)),
                ('checked_out_date', models.DateTimeField(blank=True, null=True)),
                ('check_out_department', models.CharField(blank=True, max_length=100, null=True)),
                ('check_out_notes', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('danger', 'Checked In - Stored'), ('warning', 'Checked Out - On Long Term Loan'), ('primary', 'Checked In - Ready for Use'), ('secondary', 'In Transit - Transporting'), ('success', 'Checked Out - In Use'), ('info', 'Decommissioned')], default='primary', max_length=15)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='furry.profile')),
                ('storage_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.area')),
            ],
        ),
        migrations.CreateModel(
            name='AssetLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('entry', models.TextField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.asset')),
                ('user_match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='furry.profile')),
            ],
        ),
    ]
