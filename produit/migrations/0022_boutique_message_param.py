# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0021_boutique_users_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='boutique',
            name='message_param',
            field=models.TextField(default='hello'),
        ),
    ]
