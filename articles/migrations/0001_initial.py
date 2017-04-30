# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-28 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.TextField(blank=True, help_text='The title of the article')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='The body text of the article')),
            ],
            options={
                'verbose_name': 'Article',
            },
            bases=('wagtailcore.page',),
        ),
    ]
