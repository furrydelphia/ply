# Generated by Django 4.2.4 on 2023-12-07 23:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0020_remove_communitystaff_id_communitystaff_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communityadmins',
            name='id',
        ),
        migrations.AddField(
            model_name='communityadmins',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]