# Generated by Django 4.2.4 on 2024-01-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0016_streamprofilexmppsettings_enable_webclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamprofilexmppsettings',
            name='join_group_mucs',
            field=models.BooleanField(default=True, help_text="When enabled, you'll be automatically added to the XMPP multi-user-chat (MUC) for any group you join on the site.", verbose_name='Automaticlaly join the XMPP MUCs for any group joined.'),
        ),
    ]
