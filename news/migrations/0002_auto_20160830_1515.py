# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
