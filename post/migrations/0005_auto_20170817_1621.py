# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20170816_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.group_based_upload_to_categorie),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
    ]
