# Generated by Django 5.1.1 on 2024-09-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(default=1, help_text='Заполнится автоматически', max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
