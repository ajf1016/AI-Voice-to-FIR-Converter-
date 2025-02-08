# Generated by Django 5.1.6 on 2025-02-08 19:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('audio_file', models.FileField(upload_to='audio_files/')),
                ('transcribed_text', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FIR',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=20, unique=True)),
                ('original_text', models.TextField()),
                ('fir_text', models.TextField()),
                ('fir_pdf', models.FileField(blank=True, null=True, upload_to='fir_pdfs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('audio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.audio')),
            ],
        ),
    ]
