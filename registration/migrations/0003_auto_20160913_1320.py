# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160912_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=100000)),
                ('pay', models.CharField(max_length=50)),
                ('deadline', models.DateTimeField(verbose_name=b'Date to complete the project till')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.RenameModel(
            old_name='job_application',
            new_name='JobApplication',
        ),
        migrations.RemoveField(
            model_name='job_details',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='job_provider',
            name='id',
        ),
        migrations.RemoveField(
            model_name='job_seeker',
            name='id',
        ),
        migrations.AlterField(
            model_name='job_provider',
            name='company_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='user_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.JobDetails'),
        ),
        migrations.DeleteModel(
            name='job_details',
        ),
        migrations.AddField(
            model_name='jobdetails',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.job_provider'),
        ),
    ]