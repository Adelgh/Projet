# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_album_boutique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='boutique',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produit.Boutique'),
        ),
    ]