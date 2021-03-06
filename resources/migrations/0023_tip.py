# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-07 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0022_auto_20170906_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('resourcepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources.ResourcePage')),
                ('tip_text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('credit', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('resources.resourcepage',),
        ),
    ]
