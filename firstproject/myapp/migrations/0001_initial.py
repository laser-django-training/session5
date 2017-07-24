# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('creationdate', models.DateTimeField()),
            ],
        ),
    ]
