# Generated by Django 2.2.20 on 2021-05-14 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210514_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='purchase_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 5, 14, 16, 46, 31, 761939, tzinfo=utc), verbose_name='Время '),
            preserve_default=False,
        ),
    ]
