# Generated by Django 5.1.1 on 2025-05-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0005_alter_meep_options_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
