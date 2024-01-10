# Generated by Django 4.2.4 on 2024-01-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0017_streamprofilexmppsettings_join_group_mucs'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamprofilexmppsettings',
            name='auto_add_friend',
            field=models.BooleanField(default=True, help_text='When enabled, any new friends you add on the site will be automatically added to your XMPP contact list as well.', verbose_name='Automatically add new friends to XMPP Contacts'),
        ),
        migrations.AlterField(
            model_name='streamprofilexmppsettings',
            name='enable_webclient',
            field=models.BooleanField(default=True, help_text='Enable/disable the embedded XMPP client for all pages on the site. This does not control/disable other XMPP Clients', verbose_name='Enable XMPP Webclient'),
        ),
        migrations.AlterField(
            model_name='streamprofilexmppsettings',
            name='join_group_mucs',
            field=models.BooleanField(default=True, help_text="When enabled, you'll be automatically added to the XMPP multi-user-chat (MUC) for any group you join on the site.", verbose_name='Automaticlaly join the XMPP MUCs for any group joined'),
        ),
    ]
