# Generated by Django 4.2.4 on 2023-11-20 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0007_registrantdata_conreglevel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrantdata',
            name='croppedImage',
        ),
        migrations.RemoveField(
            model_name='registrantdata',
            name='customUploadPicture',
        ),
        migrations.RemoveField(
            model_name='registrantdata',
            name='isCustomPicture',
        ),
        migrations.RemoveField(
            model_name='registrantdata',
            name='rId',
        ),
    ]
