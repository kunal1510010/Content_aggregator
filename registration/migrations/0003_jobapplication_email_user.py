# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160920_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='email_user',
            field=models.EmailField(default='kunal716338@gmail.com', max_length=254),
        ),
    ]