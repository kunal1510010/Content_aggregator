# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_jobapplication_email_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='height_field',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='width_field',
            field=models.IntegerField(default=100),
        ),
    ]
