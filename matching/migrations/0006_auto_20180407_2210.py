# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-07 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0005_auto_20180331_1756'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Matching_List',
        ),
        migrations.RemoveField(
            model_name='matching',
            name='request_data',
        ),
        migrations.AddField(
            model_name='matching',
            name='sequence',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
