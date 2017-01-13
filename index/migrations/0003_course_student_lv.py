# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20161214_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student_lv',
            field=models.CharField(default=b'\xe9\x80\x82\xe5\x90\x88\xe6\x89\x80\xe6\x9c\x89\xe4\xba\xba', max_length=100, verbose_name='\u9002\u5408\u5b66\u5458\u6c34\u5e73'),
        ),
    ]
