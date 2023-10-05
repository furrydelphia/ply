# Generated by Django 4.0.4 on 2023-04-30 22:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0010_alter_registrant_addr1_alter_registrant_addr2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrant',
            name='id',
        ),
        migrations.AddField(
            model_name='registrant',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
