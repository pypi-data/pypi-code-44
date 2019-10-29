# Generated by Django 2.2.6 on 2019-10-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_data_manager", "0010_auto_20191002_1521")]

    operations = [
        migrations.AlterField(
            model_name="historicalqueryrule",
            name="rule_handler_name",
            field=models.CharField(
                choices=[("do_nothing", "Do Nothing"), ("default", "Default")],
                default="default",
                max_length=150,
            ),
        ),
        migrations.AlterField(
            model_name="queryrule",
            name="rule_handler_name",
            field=models.CharField(
                choices=[("do_nothing", "Do Nothing"), ("default", "Default")],
                default="default",
                max_length=150,
            ),
        ),
    ]
