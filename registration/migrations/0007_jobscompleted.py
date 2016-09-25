# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20160922_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsCompleted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='guest', max_length=40)),
                ('details', models.CharField(default='guest', max_length=10000)),
                ('user_name', models.CharField(default='guest', max_length=20)),
                ('pay_given', models.IntegerField(default=0)),
            ],
        ),
    ]