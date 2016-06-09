# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_quiz_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(max_length=500, verbose_name='answer choice text'),
        ),
        migrations.AlterField(
            model_name='explanation',
            name='text',
            field=models.TextField(max_length=500, verbose_name='explanation text'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=500, verbose_name='question text'),
        ),
    ]
