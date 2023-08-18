# Generated by Django 4.2.4 on 2023-08-15 20:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0002_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiceEvent',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Event Created')),
                ('type', models.TextField(verbose_name='Event Type')),
                ('count', models.IntegerField(default=1, verbose_name='Dice Count')),
                ('sides', models.IntegerField(default=12, verbose_name='Number of Sides')),
                ('contents_json', models.JSONField(blank=True, null=True, verbose_name='Verbose Event Data')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Author')),
            ],
            options={
                'db_table': 'roleplaying_plydice_dice_event',
            },
        ),
        migrations.CreateModel(
            name='DiceRoll',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Roll Time')),
                ('type', models.TextField(verbose_name='Roll Type')),
                ('count', models.IntegerField(default=1, verbose_name='Dice Count')),
                ('sides', models.IntegerField(default=12, verbose_name='Number of Sides')),
                ('result', models.IntegerField(default=0, verbose_name='Results ')),
                ('threshold', models.IntegerField(default=6, verbose_name='Threshold ')),
                ('contents_json', models.JSONField(blank=True, null=True, verbose_name='Verbose Roll Data')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Profile')),
            ],
            options={
                'db_table': 'roleplaying_plydice_dice_roll',
            },
        ),
        migrations.CreateModel(
            name='DiceEventRoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plydice.diceevent', verbose_name='Event')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plydice.diceroll', verbose_name='Roll')),
            ],
            options={
                'db_table': 'roleplaying_plydice_dice_event_roll',
            },
        ),
        migrations.AddConstraint(
            model_name='diceeventroll',
            constraint=models.UniqueConstraint(fields=('event', 'roll'), name='unique_roll'),
        ),
    ]