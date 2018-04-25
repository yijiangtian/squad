# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_group_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='expected_test_runs',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='environment',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='notification_timeout',
            field=models.IntegerField(blank=True, help_text='Force sending build notifications after this many seconds', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='wait_before_notification',
            field=models.IntegerField(blank=True, help_text='Wait this many seconds before sending notifications', null=True),
        ),
    ]