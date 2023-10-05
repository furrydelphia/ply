# Generated by Django 3.2.4 on 2021-06-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staffassignment",
            name="rank",
            field=models.CharField(
                choices=[
                    ("Staff", "Staff Member"),
                    ("Department Assistant Director", "Department Assistant Director"),
                    ("Department Director", "Department Director"),
                    ("Board Member", "Board Member"),
                ],
                max_length=50,
            ),
        ),
    ]
