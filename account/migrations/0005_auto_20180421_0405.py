# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-21 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_firebase_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='rating_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='rating_sum',
            field=models.IntegerField(default=0),
        ),
    ]
