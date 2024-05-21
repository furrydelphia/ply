# Generated by Django 4.2.4 on 2024-04-14 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0013_galleryenabledplugins"),
    ]

    operations = [
        migrations.AddField(
            model_name="gallerycoresettings",
            name="enabled_plugins",
            field=models.ManyToManyField(
                to="core.galleryplugins", verbose_name="Enabled Gallery Plugins"
            ),
        ),
    ]