# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history_and_future_of_the_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('file_position', models.CharField(max_length=200)),
                ('kwicl', models.TextField()),
                ('keyword', models.CharField(max_length=200)),
                ('kwicr', models.TextField()),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('correct_choice', models.CharField(max_length=200)),
            ],
        ),
    ]
