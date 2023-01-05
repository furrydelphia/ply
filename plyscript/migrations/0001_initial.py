# Generated by Django 4.0.4 on 2022-08-19 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0005_friend_community'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.TextField(default='application/ply.script.generic', verbose_name='Script Type')),
                ('name', models.TextField(verbose_name='Script Name')),
                ('descr', models.TextField(verbose_name='Script Description')),
                ('function_name', models.TextField(verbose_name='Script Funcname')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Script Created/updated')),
                ('body', models.TextField(default=6, verbose_name='Script Body')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]