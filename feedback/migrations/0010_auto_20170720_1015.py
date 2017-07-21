# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 10:15
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0009_auto_20170720_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customformsubmission',
            name='page',
        ),
        migrations.RemoveField(
            model_name='customformsubmission',
            name='user',
        ),
        migrations.RemoveField(
            model_name='feedbackpage',
            name='alpha',
        ),
        migrations.RemoveField(
            model_name='feedbackpage',
            name='feedback1_default_text',
        ),
        migrations.RemoveField(
            model_name='feedbackpage',
            name='feedback1_help_text',
        ),
        migrations.RemoveField(
            model_name='feedbackpage',
            name='feedback1_intro',
        ),
        migrations.RemoveField(
            model_name='feedbackpage',
            name='feedback2_default_text',
        ),
        migrations.RemoveField(
            model_name='feedbackpage',
            name='feedback2_help_text',
        ),
        migrations.RemoveField(
            model_name='feedbackpage',
            name='feedback2_intro',
        ),
        migrations.RemoveField(
            model_name='feedbackpage',
            name='form_title',
        ),
        migrations.AlterField(
            model_name='formfield',
            name='after_input',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='after input'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='before_input',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='before input'),
        ),
        migrations.DeleteModel(
            name='CustomFormSubmission',
        ),
    ]
