# Generated by Django 5.1.1 on 2024-09-20 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_remove_video_image_alter_video_create_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(help_text='Заполнится автоматически', max_length=255, verbose_name='URL'),
        ),
    ]
