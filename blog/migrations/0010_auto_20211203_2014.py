# Generated by Django 2.0 on 2021-12-03 20:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211203_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 20, 14, 17, 473922, tzinfo=utc)),
        ),
    ]
