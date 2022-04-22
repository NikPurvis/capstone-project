# Generated by Django 4.0.4 on 2022-04-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=4)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=13)),
                ('genre', models.CharField(max_length=100)),
                ('olid', models.CharField(max_length=25)),
            ],
        ),
    ]
