# Generated by Django 2.0 on 2018-08-08 12:14

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0063_merge_20180611_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.TextField(max_length=250)),
                ('default_flag', models.BooleanField(default=False)),
                ('respond_hours', models.BigIntegerField()),
                ('plan_within', models.BigIntegerField()),
                ('resolution_hours', models.BigIntegerField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='ticket',
            name='sla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='djconnectwise.Sla'),
        ),
    ]
