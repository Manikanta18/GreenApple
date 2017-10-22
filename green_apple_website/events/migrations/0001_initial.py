# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('image', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
