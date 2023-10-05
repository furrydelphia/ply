# Generated by Django 3.1.3 on 2022-05-08 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0009_auto_20220405_1823'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HotTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('selected_day', models.CharField(choices=[('F', 'Friday'), ('S', 'Saturday')], default='F', max_length=1)),
                ('intended_selling', models.TextField(default='', help_text='What do you intend on selling at your Hot Table? This can be anything from normal wares to specialized, 18+ items/art/clothing/etc.')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('space_name', models.CharField(help_text='Name in physical location', max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.event')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('data', models.JSONField(default=dict)),
                ('paid', models.BooleanField(default=False)),
                ('invoice_type', models.CharField(choices=[('reg', 'Registration Invoice'), ('table', 'Table Invoice'), ('general', 'General Invoice')], default='general', max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('square_code', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_collected', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_paid', models.DateTimeField(blank=True, null=True)),
                ('date_due', models.DateTimeField(blank=True, null=True)),
                ('reference_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('checkout_id', models.CharField(blank=True, max_length=250, null=True)),
                ('idempotency_key', models.UUIDField(default=uuid.uuid4)),
                ('debug_result_data', models.JSONField(default=dict)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
