# Generated by Django 2.2.2 on 2019-08-06 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("edc_data_manager", "0002_auto_20190725_1822")]

    operations = [
        migrations.RemoveField(model_name="dataquery", name="tcc_user"),
        migrations.RemoveField(model_name="historicaldataquery", name="tcc_user"),
        migrations.AddField(
            model_name="dataquery",
            name="dm_user",
            field=models.ForeignKey(
                blank=True,
                help_text="select a name from the list",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="dm_user",
                to="edc_data_manager.DataManagerUser",
                verbose_name="DM resolved by",
            ),
        ),
        migrations.AddField(
            model_name="historicaldataquery",
            name="dm_user",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="select a name from the list",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_data_manager.DataManagerUser",
                verbose_name="DM resolved by",
            ),
        ),
        migrations.AlterField(
            model_name="dataquery",
            name="resolved_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="DM resolved on"
            ),
        ),
        migrations.AlterField(
            model_name="dataquery",
            name="site_response_status",
            field=models.CharField(
                choices=[
                    ("New", "New"),
                    ("open", "Open"),
                    ("feedback", "Feedback, awaiting data manager"),
                    ("resolved", "Resolved"),
                ],
                default="New",
                max_length=25,
                verbose_name="Site status",
            ),
        ),
        migrations.AlterField(
            model_name="dataquery",
            name="status",
            field=models.CharField(
                choices=[
                    ("open", "Open, awaiting site"),
                    ("closed", "Closed"),
                    ("closed_with_action", "Closed, with plan of action"),
                ],
                default="open",
                max_length=25,
                verbose_name="DM status",
            ),
        ),
        migrations.AlterField(
            model_name="dataquery",
            name="title",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="historicaldataquery",
            name="resolved_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="DM resolved on"
            ),
        ),
        migrations.AlterField(
            model_name="historicaldataquery",
            name="site_response_status",
            field=models.CharField(
                choices=[
                    ("New", "New"),
                    ("open", "Open"),
                    ("feedback", "Feedback, awaiting data manager"),
                    ("resolved", "Resolved"),
                ],
                default="New",
                max_length=25,
                verbose_name="Site status",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldataquery",
            name="status",
            field=models.CharField(
                choices=[
                    ("open", "Open, awaiting site"),
                    ("closed", "Closed"),
                    ("closed_with_action", "Closed, with plan of action"),
                ],
                default="open",
                max_length=25,
                verbose_name="DM status",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldataquery",
            name="title",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
