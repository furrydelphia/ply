# Generated by Django 4.2.4 on 2023-08-15 20:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('group', '0001_initial'),
        ('keywords', '0001_initial'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagesPerStreamView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_created', models.DateTimeField(verbose_name='Stream Created')),
                ('stream_type', models.TextField(verbose_name='Stream Type')),
                ('stream_icon', models.TextField(blank=True, null=True, verbose_name='Stream Icon')),
                ('stream_shares', models.IntegerField(default=0, verbose_name='Share Count')),
                ('stream_views', models.IntegerField(default=0, verbose_name='Views Count')),
                ('stream_nodes', models.IntegerField(default=0, verbose_name='Node Count')),
                ('stream_archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('stream_hidden', models.BooleanField(default=False, verbose_name='Hidden FLAG')),
                ('stream_system', models.BooleanField(default=False, verbose_name='System FLAG')),
                ('stream_group_id', models.UUIDField(verbose_name='Stream Group UUID')),
                ('profile_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('profile_created', models.DateTimeField(auto_now_add=True, verbose_name='Profile Created')),
                ('profile_last_seen', models.DateTimeField(auto_now_add=True, verbose_name='Profile Last Seen Online')),
                ('profile_age', models.TextField(blank=True, default=1, verbose_name='Current Age')),
                ('profile_name', models.TextField(verbose_name='Name')),
                ('profile_status', models.TextField(blank=True, default='CITIZEN', verbose_name='status')),
                ('profile_species', models.TextField(default='Sentient', verbose_name='Species')),
                ('profile_introduction', models.TextField(verbose_name='Profile Intro')),
                ('profile_pronouns', models.TextField(max_length=200, verbose_name='Pronouns')),
                ('profile_gender', models.TextField(max_length=200, verbose_name='Gender')),
                ('profile_avatar', models.TextField(blank=True, null=True, verbose_name='Avatar URL')),
                ('profile_posts', models.IntegerField(default=0, verbose_name='Post Count')),
                ('profile_views', models.IntegerField(default=0, verbose_name='Post Count')),
                ('profile_nodes', models.IntegerField(default=0, verbose_name='Node Count')),
                ('profile_blocked', models.BooleanField(default=False, verbose_name='Blocked FLAG')),
                ('profile_frozen', models.BooleanField(default=False, verbose_name='Frozen FLAG')),
                ('profile_system', models.BooleanField(default=False, verbose_name='System FLAG')),
                ('message_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('message_created', models.DateTimeField(auto_now_add=True, verbose_name='Stream Created')),
                ('message_type', models.TextField(verbose_name='Message Type')),
                ('message_icon', models.TextField(blank=True, null=True, verbose_name='Message Icon')),
                ('reposts', models.IntegerField(default=0, verbose_name='Reposts Count')),
                ('replies', models.IntegerField(default=0, verbose_name='Replies Count')),
                ('shares', models.IntegerField(default=0, verbose_name='Share Count')),
                ('likes', models.IntegerField(default=0, verbose_name='Like Count')),
                ('threads', models.IntegerField(default=0, verbose_name='Thread Count')),
                ('views', models.IntegerField(default=0, verbose_name='Views Count')),
                ('contents_text', models.TextField(blank=True, max_length=500, null=True, verbose_name='Stream Content: Text Type')),
                ('contents_text_parsed', models.TextField(blank=True, null=True, verbose_name='Stream Content: Text Type (Parsed)')),
                ('contents_json', models.JSONField(blank=True, null=True, verbose_name='Stream Content: JSON Type')),
                ('contents_bin', models.BinaryField(blank=True, null=True, verbose_name='Stream Content: Binary Type')),
            ],
            options={
                'db_table': 'communities_stream_stream_message_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Stream Created')),
                ('type', models.TextField(verbose_name='Stream Type (internal)')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Stream Name')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='Stream Description')),
                ('tag', models.TextField(blank=True, null=True, verbose_name='Stream Tag')),
                ('default_perm', models.TextField(default='e', verbose_name='Stream Default Permission')),
                ('icon', models.TextField(blank=True, null=True, verbose_name='Stream Icon')),
                ('shares', models.IntegerField(default=0, verbose_name='Share Count')),
                ('views', models.IntegerField(default=0, verbose_name='Views Count')),
                ('nodes', models.IntegerField(default=0, verbose_name='Node Count')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden FLAG')),
                ('system', models.BooleanField(default=False, verbose_name='System FLAG')),
                ('opened', models.BooleanField(default=False, verbose_name='Stream FLAG: has been Opened')),
                ('root_stream', models.BooleanField(default=False, verbose_name='Root Stream FLAG')),
                ('bkg1', models.TextField(default='#ffffff', verbose_name='Stream Bkg Colour #1')),
                ('bkg2', models.TextField(default='#ffffff', verbose_name='Stream Bkg Colour #2')),
                ('bkgt', models.TextField(default='s1', verbose_name='Stream Bkg Type')),
                ('opacity1', models.DecimalField(decimal_places=3, default=0, max_digits=5, verbose_name='Stream Bkg Opacity #1')),
                ('opacity2', models.DecimalField(decimal_places=3, default=0, max_digits=5, verbose_name='Stream Bkg Opacity #2')),
                ('midpoint', models.IntegerField(default=50, verbose_name='Stream Bkg Midpoint ')),
                ('angle', models.IntegerField(default=90, verbose_name='Stream Bkg Midpoint ')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='community.community', verbose_name='Community')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='group.group', verbose_name='Group')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Profile')),
            ],
            options={
                'db_table': 'communities_stream_stream',
            },
        ),
        migrations.CreateModel(
            name='StreamMessage',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Stream Created')),
                ('type', models.TextField(verbose_name='Message Type')),
                ('icon', models.TextField(blank=True, null=True, verbose_name='Message Icon')),
                ('reposts', models.IntegerField(default=0, verbose_name='Reposts Count')),
                ('replies', models.IntegerField(default=0, verbose_name='Replies Count')),
                ('shares', models.IntegerField(default=0, verbose_name='Share Count')),
                ('likes', models.IntegerField(default=0, verbose_name='Like Count')),
                ('threads', models.IntegerField(default=0, verbose_name='Thread Count')),
                ('views', models.IntegerField(default=0, verbose_name='Views Count')),
                ('contents_text', models.TextField(blank=True, max_length=500, null=True, verbose_name='Stream Content: Text Type')),
                ('contents_text_parsed', models.TextField(blank=True, null=True, verbose_name='Stream Content: Text Type (Parsed)')),
                ('contents_json', models.JSONField(blank=True, null=True, verbose_name='Stream Content: JSON Type')),
                ('contents_bin', models.BinaryField(blank=True, null=True, verbose_name='Stream Content: Binary Type')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='profiles.profile', verbose_name='Author')),
                ('posted_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stream.stream', verbose_name='Posted in Stream')),
                ('references', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stream.streammessage', verbose_name='References')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream.stream', verbose_name='Stream')),
            ],
            options={
                'db_table': 'communities_stream_stream_message',
            },
        ),
        migrations.CreateModel(
            name='StreamType',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Type Created')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Type Name')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='Type Descr')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='community.community', verbose_name='Community')),
            ],
            options={
                'db_table': 'communities_stream.stream_type',
            },
        ),
        migrations.CreateModel(
            name='StreamThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.TextField(max_length=200, verbose_name='Hash')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Thread Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Thread Updated')),
                ('items', models.IntegerField(default=0, verbose_name='Item Count')),
                ('views', models.IntegerField(default=0, verbose_name='Views Count')),
                ('likes', models.IntegerField(default=0, verbose_name='Likes Count')),
                ('dislikes', models.IntegerField(default=0, verbose_name='DisLikes Count')),
                ('shares', models.IntegerField(default=0, verbose_name='Shares Count')),
                ('comments', models.IntegerField(default=0, verbose_name='Comment Count')),
                ('active', models.BooleanField(default=True, verbose_name='Active FLAG')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden FLAG')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream.stream', verbose_name='Stream')),
            ],
            options={
                'db_table': 'communities_stream_stream_thread',
            },
        ),
        migrations.CreateModel(
            name='StreamSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Notification Inbox Created')),
                ('last_view', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Last Viewed')),
                ('archived', models.BooleanField(default=False, verbose_name='Archived FLAG')),
                ('hidden', models.BooleanField(default=False, verbose_name='Hidden FLAG')),
                ('system', models.BooleanField(default=False, verbose_name='System FLAG')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.community', verbose_name='Community')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream.stream', verbose_name='Notification')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='profiles.profile', verbose_name='Subscriber Profile')),
            ],
            options={
                'db_table': 'communities_stream_stream_subscriber',
            },
        ),
        migrations.CreateModel(
            name='StreamMessageKeywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keywords.keyword', verbose_name='Keyword')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream.streammessage', verbose_name='Message')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream.stream', verbose_name='Stream')),
            ],
            options={
                'db_table': 'communities_stream_stream_message_keywords',
            },
        ),
        migrations.AddField(
            model_name='stream',
            name='streamtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='stream.streamtype', verbose_name='Stream Type (public)'),
        ),
        migrations.AddConstraint(
            model_name='streamtype',
            constraint=models.UniqueConstraint(fields=('name', 'community'), name='unique_stream_type'),
        ),
        migrations.AddConstraint(
            model_name='stream',
            constraint=models.UniqueConstraint(fields=('tag', 'profile', 'community'), name='unique_stream_tag'),
        ),
    ]