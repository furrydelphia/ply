# Generated by Django 4.0.4 on 2023-03-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0013_staffassignment_grant_access_to_management_panel'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffassignment',
            name='permissions_matrix',
            field=models.JSONField(blank=True, default={'app-manage': {'edit': False, 'manage': False, 'view': False}, 'events-manage': {'edit': False, 'manage': False, 'view': False}, 'marketplace-manage': {'edit': False, 'manage': False, 'view': False}, 'registration-manage': {'edit': False, 'manage': False, 'view': False}, 'staff-manage': {'edit': False, 'manage': False, 'view': False}, 'staff-portal': {'edit': False, 'manage': False, 'view': False}, 'volunteer-manage': {'edit': False, 'manage': False, 'view': False}, 'volunteer-portal': {'edit': False, 'manage': False, 'view': False}}, null=True),
        ),
    ]
