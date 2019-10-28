# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-19 09:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MapStoreAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[(b'string', b'String'), (b'number', b'Number'), (b'integer', b'Integer'), (b'boolean', b'Boolean'), (b'binary', b'Binary')], max_length=80)),
                ('value', models.TextField(blank=True, db_column=b'value')),
            ],
        ),
        migrations.CreateModel(
            name='MapStoreData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blob', jsonfield.fields.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='MapStoreResource',
            fields=[
                ('id', models.BigIntegerField(blank=True, null=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('attributes', models.ManyToManyField(blank=True, null=True, related_name='attributes', to='mapstore2_adapter.MapStoreAttribute')),
                ('data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data', to='mapstore2_adapter.MapStoreData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mapstoredata',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapstore2_adapter.MapStoreResource'),
        ),
        migrations.AddField(
            model_name='mapstoreattribute',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapstore2_adapter.MapStoreResource'),
        ),
        migrations.AddIndex(
            model_name='mapstoreresource',
            index=models.Index(fields=[b'id'], name='mapstore2_a_id_cd23a9_idx'),
        ),
        migrations.AddIndex(
            model_name='mapstoreresource',
            index=models.Index(fields=[b'name'], name='mapstore2_a_name_35c0a1_idx'),
        ),
    ]
