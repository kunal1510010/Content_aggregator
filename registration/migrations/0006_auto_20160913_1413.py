# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20160913_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='id',
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]