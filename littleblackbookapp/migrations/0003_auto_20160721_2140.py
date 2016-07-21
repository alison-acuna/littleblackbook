# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('littleblackbookapp', '0002_auto_20160721_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('website', models.URLField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='professional',
            name='goals',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='professionals',
            field=models.ManyToManyField(to='littleblackbookapp.Professional'),
        ),
    ]
