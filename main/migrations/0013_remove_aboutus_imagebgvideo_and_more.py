# Generated by Django 5.2.3 on 2025-06-25 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_aboutus_imagebgvideo_aboutus_video_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='imagebgvideo',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='video_file',
        ),
    ]
