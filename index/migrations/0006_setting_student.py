# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_coupon_favourable_favourableproduct_payway_setting_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='student',
            field=models.OneToOneField(related_name='setting_student', default=b'', verbose_name='\u5b66\u751f', to='index.Student'),
        ),
    ]
