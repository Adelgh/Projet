# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20170817_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to=post.models.group_based_upload_to_categori),
        ),
    ]
