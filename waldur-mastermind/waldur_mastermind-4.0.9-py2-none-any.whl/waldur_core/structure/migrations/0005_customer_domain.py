# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-04 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0004_customer_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='domain',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
