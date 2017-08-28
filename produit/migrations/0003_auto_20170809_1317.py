# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import produit.models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to=produit.models.group_based_upload_to)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='categorie',
        ),
    ]
