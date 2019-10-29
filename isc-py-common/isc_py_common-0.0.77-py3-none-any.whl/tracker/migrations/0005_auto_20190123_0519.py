# Generated by Django 2.1.5 on 2019-01-23 05:19

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import isc_common.fields.related


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0004_auto_20190121_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages_theme',
            options={'verbose_name': 'Темы сообщений'},
        ),
        migrations.AddField(
            model_name='messages',
            name='to_whom',
            field=isc_common.fields.related.ForeignKeyCascade(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='to_whom', to=settings.AUTH_USER_MODEL),
        ),
    ]
