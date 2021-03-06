# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 11:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produit', '0023_auto_20170824_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wishlist', models.ManyToManyField(related_name='produit', to='produit.Produit')),
            ],
        ),
    ]
