# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0086_cartitem_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentusage',
            name='billing_period',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='componentusage',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterUniqueTogether(
            name='componentusage',
            unique_together=set([('resource', 'component', 'plan_period', 'billing_period')]),
        ),
    ]
