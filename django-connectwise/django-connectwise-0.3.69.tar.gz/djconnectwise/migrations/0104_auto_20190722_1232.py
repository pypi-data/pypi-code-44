# Generated by Django 2.1 on 2019-07-22 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0103_activitystatus_activitytype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitystatus',
            options={'ordering': ('name',), 'verbose_name_plural': 'activity statuses'},
        ),
    ]
