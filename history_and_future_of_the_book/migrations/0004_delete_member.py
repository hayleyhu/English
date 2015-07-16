# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history_and_future_of_the_book', '0003_member'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]
