# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-30 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0027_allow_svg_for_offering_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
