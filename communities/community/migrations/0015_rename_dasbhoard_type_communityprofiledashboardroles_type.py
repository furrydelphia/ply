# Generated by Django 4.2.4 on 2023-12-07 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0014_rename_dashboard_type_communitydashboardtype_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communityprofiledashboardroles',
            old_name='dasbhoard_type',
            new_name='type',
        ),
    ]