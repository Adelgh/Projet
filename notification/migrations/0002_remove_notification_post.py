# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='post',
        ),
    ]
