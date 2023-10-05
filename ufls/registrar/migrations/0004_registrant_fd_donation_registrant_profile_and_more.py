# Generated by Django 4.0.4 on 2023-04-15 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furry', '0011_registrantassociationkey'),
        ('registrar', '0003_registrantlevel_registrant_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrant',
            name='fd_donation',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Furrydelphia Donation'),
        ),
        migrations.AddField(
            model_name='registrant',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='furry.profile', verbose_name='Registrant Profile'),
        ),
        migrations.AddField(
            model_name='registrantlevel',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Level Active Flag'),
        ),
    ]
