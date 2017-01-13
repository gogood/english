# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_setting_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='star_number',
            field=models.FloatField(verbose_name='\u661f\u661f\u6570'),
        ),
    ]
