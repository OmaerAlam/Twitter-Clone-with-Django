# Generated by Django 5.1.1 on 2025-05-14 07:48

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0006_alter_profile_date_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='profile',
            name='data_modified',
            field=models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
