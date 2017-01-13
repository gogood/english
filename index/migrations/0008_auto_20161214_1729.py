# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20161214_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=20, verbose_name='\u5b66\u53f7'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='shared_number',
            field=models.IntegerField(verbose_name='\u5206\u4eab\u6570'),
        ),
    ]
