# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-04 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.CharField(blank=True, max_length=255, null=True)),
                ('customer', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='doing', max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('timeupdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
