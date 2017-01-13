# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_auto_20161215_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docsite',
            name='type',
        ),
        migrations.AddField(
            model_name='docsite',
            name='type_name',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6587\u6863\u7c7b\u578b\u540d', choices=[(0, '\u590d\u4e60'), (1, '\u9884\u4e60')]),
        ),
        migrations.DeleteModel(
            name='DocType',
        ),
    ]
