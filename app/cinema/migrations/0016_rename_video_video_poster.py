# Generated by Django 5.1.1 on 2024-10-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0015_video_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='poster',
        ),
    ]
