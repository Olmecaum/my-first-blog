# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-04 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171204_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'matrices/%Y/%m/%D/'),
        ),
    ]