# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-22 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20170605_1555'),
    ]

    operations = [
        migrations.RenameModel('CategoryTag', 'IssueTag'),
        migrations.RenameModel('AudienceTag', 'ReasonTag')
    ]
