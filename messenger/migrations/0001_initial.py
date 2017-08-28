# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 08:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import messenger.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
                ('objet', models.TextField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to=messenger.models.group_based_upload_to_seconder)),
                ('url', models.TextField(blank=True, max_length=1000, null=True)),
                ('commercant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produit.Commercant')),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produit.Produit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date',),
                'db_table': 'messages_message',
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]