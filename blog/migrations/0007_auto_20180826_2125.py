# Generated by Django 2.0.5 on 2018-08-26 21:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180826_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 21, 25, 2, 643756, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 21, 25, 2, 643308, tzinfo=utc)),
        ),
    ]
