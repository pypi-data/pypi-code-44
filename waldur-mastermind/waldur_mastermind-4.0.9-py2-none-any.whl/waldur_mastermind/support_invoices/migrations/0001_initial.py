# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-08 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('support', '0027_non_unique_template_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestBasedOffering',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('support.offering',),
        ),
    ]
