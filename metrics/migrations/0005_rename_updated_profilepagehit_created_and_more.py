# Generated by Django 4.0.2 on 2022-04-27 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_initial'),
        ('group', '0002_initial'),
        ('profiles', '0001_initial'),
        ('metrics', '0004_alter_galleryitemhit_group_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilepagehit',
            old_name='updated',
            new_name='created',
        ),
        migrations.AddField(
            model_name='profilepagehit',
            name='remote_addr',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='remote address'),
        ),
        migrations.AddField(
            model_name='profilepagehit',
            name='user_agent',
            field=models.TextField(blank=True, db_index=True, verbose_name='Hit User Agent'),
        ),
        migrations.AlterField(
            model_name='profilepagehit',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='community.community', verbose_name='Community'),
        ),
        migrations.AlterField(
            model_name='profilepagehit',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='group.group', verbose_name='viewed by member of group'),
        ),
        migrations.AlterField(
            model_name='profilepagehit',
            name='visitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='profiles.profile', verbose_name='Viewed by Profile'),
        ),
    ]
