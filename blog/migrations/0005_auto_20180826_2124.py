# Generated by Django 2.0.5 on 2018-08-26 21:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180826_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 21, 24, 11, 96468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 21, 24, 11, 95934, tzinfo=utc)),
        ),
    ]
