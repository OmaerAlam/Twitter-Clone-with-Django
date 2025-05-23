# Generated by Django 5.1.1 on 2025-05-13 09:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0003_rename_data_modified_profile_date_modified_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meep',
            options={'ordering': ['-created_at'], 'verbose_name': 'Meep', 'verbose_name_plural': 'Meeps'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='meep',
            name='body',
            field=models.CharField(max_length=280),
        ),
        migrations.AlterField(
            model_name='meep',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='meep_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='homepage_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
