# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.CharField(default='doing', max_length=255),
        ),
    ]
