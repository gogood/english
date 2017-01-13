# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_teachcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachcourse',
            name='note',
            field=models.CharField(default=b'\xe5\x87\x86\xe6\x97\xb6\xe4\xb8\x8a\xe8\xaf\xbe', max_length=100, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='teachcourse',
            name='course_time',
            field=models.DateTimeField(verbose_name='\u4e0a\u8bfe\u65f6\u95f4'),
        ),
    ]
