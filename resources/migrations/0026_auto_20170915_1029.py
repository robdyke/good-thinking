# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-15 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0025_remove_resourcepage_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='header',
            field=models.TextField(blank=True, help_text='Hero title'),
        ),
        migrations.AlterField(
            model_name='main',
            name='header',
            field=models.TextField(blank=True, help_text='Hero title'),
        ),
    ]