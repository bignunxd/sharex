# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-31 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20180324_1704'),
        ('request', '0007_request_fare'),
        ('matching', '0003_auto_20180320_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matching',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='matching',
            name='driver',
        ),
        migrations.AddField(
            model_name='matching',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='request.Request'),
        ),
        migrations.AddField(
            model_name='matching',
            name='travel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.Travel'),
        ),
    ]
