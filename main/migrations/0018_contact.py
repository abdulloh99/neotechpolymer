# Generated by Django 5.2.3 on 2025-06-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_yangiliklar_desc2_alter_yangiliklar_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.TextField(max_length=40)),
                ('Tel', models.TextField(max_length=40, verbose_name='TEl NOMER')),
                ('facebook', models.TextField(max_length=50)),
                ('insta', models.TextField(max_length=50)),
                ('telegram', models.TextField(max_length=50)),
                ('mail', models.TextField(max_length=50)),
                ('Ishvaqti', models.TextField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'KONTAKT INFO',
            },
        ),
    ]
