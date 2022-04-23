# Generated by Django 4.0.2 on 2022-02-23 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dynapages', '0021_remove_widget_widget_id_widget_widget_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0033_profile_shield_profile_stun_profile_max_shield_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlmanacPage',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('page_id', models.TextField(max_length=200, unique=True, verbose_name='Page ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Page Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Page Updated')),
                ('introduction', models.TextField(verbose_name='Page Intro')),
                ('avatar', models.TextField(blank=True, null=True, verbose_name='Avatar URL')),
                ('posts', models.IntegerField(default=0, verbose_name='Post Count')),
                ('views', models.IntegerField(default=0, verbose_name='View Count')),
                ('nodes', models.IntegerField(default=0, verbose_name='Node Count')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('blocked', models.BooleanField(default=False, verbose_name='Blocked FLAG')),
                ('frozen', models.BooleanField(default=False, verbose_name='Frozen FLAG')),
                ('system', models.BooleanField(default=False, verbose_name='System FLAG')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='profiles.profile', verbose_name='Creator Profile')),
                ('dynaPage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='dynapages.page')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='PageText',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Page Text Created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Page Updated')),
                ('language', models.TextField(max_length=5, unique=True, verbose_name='Page Language')),
                ('page_contents', models.TextField(unique=True, verbose_name='Page Contents')),
                ('current', models.BooleanField(default=False, verbose_name='current FLAG')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almanac.almanacpage', verbose_name='AlmanacPage')),
            ],
        ),
    ]