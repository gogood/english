# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_course_student_lv'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docsite',
            options={'ordering': ['doc_name'], 'managed': True, 'verbose_name': '\u6587\u6863\u8868', 'verbose_name_plural': '\u6587\u6863\u8868'},
        ),
        migrations.AlterField(
            model_name='book',
            name='course',
            field=models.ForeignKey(related_name='book_course', verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.ForeignKey(related_name='course_type', verbose_name='\u8bfe\u7a0b\u7c7b\u578b', to='index.CourseType'),
        ),
        migrations.AlterField(
            model_name='docsite',
            name='course',
            field=models.ForeignKey(related_name='doc_course', verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
    ]
