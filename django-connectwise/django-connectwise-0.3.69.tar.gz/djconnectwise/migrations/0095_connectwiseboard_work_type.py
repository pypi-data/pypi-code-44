# Generated by Django 2.1 on 2019-07-17 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0094_connectwiseboard_work_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectwiseboard',
            name='work_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djconnectwise.WorkType'),
        ),
    ]
