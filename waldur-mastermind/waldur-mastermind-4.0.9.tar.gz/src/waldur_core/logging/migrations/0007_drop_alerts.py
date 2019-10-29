# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-27 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logging', '0006_event_feed'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='alert',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='alert',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Alert',
        ),
    ]
