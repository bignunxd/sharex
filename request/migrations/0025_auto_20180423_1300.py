# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-23 13:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0024_auto_20180421_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 24, 13, 0, 51, 580600, tzinfo=utc), verbose_name='expire'),
        ),
    ]
