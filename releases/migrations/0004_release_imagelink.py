# Generated by Django 3.1.1 on 2020-10-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0003_release_releaseartist'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='imageLink',
            field=models.CharField(default='noLink', max_length=500),
        ),
    ]
