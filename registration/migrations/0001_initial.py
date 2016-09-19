# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('contact_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='job_seeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('contact_number', models.IntegerField(default=0)),
            ],
        ),
    ]
