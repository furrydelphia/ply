# Generated by Django 3.2.4 on 2021-12-31 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff_onboarding", "0002_auto_20211231_1729"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staffonboardrecord",
            name="displayNameAs",
            field=models.CharField(
                choices=[
                    ("0", "<First Name> <Last Name>"),
                    ("1", "<Fan Name> <Last Name>"),
                    ("2", "<Fan Name>"),
                ],
                default="0",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="staffonboardrecord",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="In this format: +1 555 555 5555",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="staffonboardrecord",
            name="usernameAs",
            field=models.CharField(
                choices=[
                    ("0", "<Fan Name>@staff.furrydelphia.org"),
                    ("1", "<First Initial><Last Name>@staff.furrydelphia.org"),
                    ("2", "<Fan Name First Initial><Last Name>@staff.furrydelphia.org"),
                ],
                default="0",
                max_length=1,
            ),
        ),
    ]
