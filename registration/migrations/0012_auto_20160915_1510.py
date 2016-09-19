# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20160915_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='jobdetails',
            name='job_id',
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='user_name',
            field=models.CharField(default=b'guest', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='company_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
