# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-13 11:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0055_offeringfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='max_amount',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Maximum number of plans that could be active. Plan is disabled when maximum amount is reached.', null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
