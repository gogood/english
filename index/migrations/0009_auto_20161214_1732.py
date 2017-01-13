# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20161214_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='qq',
            field=models.CharField(max_length=20, verbose_name='QQ'),
        ),
    ]
