# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170323_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='icon',
            new_name='thumnail',
        ),
    ]