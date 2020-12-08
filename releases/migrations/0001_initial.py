# Generated by Django 3.1.1 on 2020-10-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('releaseDesc', models.CharField(max_length=6000)),
                ('releaseLink', models.CharField(max_length=6000)),
                ('releaseDate', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
    ]
