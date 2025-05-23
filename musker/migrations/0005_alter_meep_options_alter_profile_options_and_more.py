# Generated by Django 5.1.1 on 2025-05-13 15:27

import django.contrib.auth.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0004_alter_meep_options_alter_profile_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meep',
            options={},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AlterField(
            model_name='meep',
            name='body',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='meep',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='meep_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='homepage_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
