# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0015_auto_20170821_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='genrt',
            new_name='genrct',
        ),
    ]
