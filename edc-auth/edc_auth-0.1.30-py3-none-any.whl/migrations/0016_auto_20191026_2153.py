# Generated by Django 2.2.6 on 2019-10-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_auth', '0015_auto_20191026_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='short_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='role',
            name='display_name',
            field=models.CharField(db_index=True, help_text='(suggest 40 characters max.)',
                                   max_length=250, unique=True, verbose_name='Display Name'),
        ),
    ]
