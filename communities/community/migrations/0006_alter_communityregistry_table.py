# Generated by Django 4.2.4 on 2023-10-09 01:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0005_alter_community_icon_alter_community_logo_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="communityregistry",
            table="communities_community_registry",
        ),
    ]