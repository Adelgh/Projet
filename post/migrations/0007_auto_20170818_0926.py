# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20170817_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(default='2', null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Categorie'),
        ),
    ]
