# Generated by Django 5.1.6 on 2025-02-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policeofficer',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
