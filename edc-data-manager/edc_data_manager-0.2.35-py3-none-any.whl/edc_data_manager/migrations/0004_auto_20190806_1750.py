# Generated by Django 2.2.2 on 2019-08-06 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("edc_data_manager", "0003_auto_20190806_1749")]

    operations = [
        migrations.AlterUniqueTogether(
            name="dataquery",
            unique_together={
                ("registered_subject", "rule_reference", "visit_schedule")
            },
        )
    ]
