# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 20:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reaction', '0003_auto_20170814_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_reaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
