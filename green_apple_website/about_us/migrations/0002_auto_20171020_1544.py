# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutUs',
            new_name='MemberDetail',
        ),
    ]
