# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-10 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def populate_internal_ip_settings(apps, schema_editor):
    InternalIP = apps.get_model('openstack_tenant', 'InternalIP')
    for internal_ip in InternalIP.objects.all():
        internal_ip.settings = internal_ip.subnet.settings
        internal_ip.save()


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_immutable_default_json'),
        ('openstack_tenant', '0036_instance_shared_ips'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalip',
            name='settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='structure.ServiceSettings'),
        ),
        migrations.AlterField(
            model_name='internalip',
            name='backend_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='internalip',
            unique_together=set([('backend_id', 'settings')]),
        ),
        migrations.RunPython(populate_internal_ip_settings, elidable=True),
    ]
