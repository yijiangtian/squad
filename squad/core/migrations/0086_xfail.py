# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0085_projectstatus_defaults'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectstatus',
            name='tests_xfail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='status',
            name='tests_xfail',
            field=models.IntegerField(default=0),
        ),
    ]