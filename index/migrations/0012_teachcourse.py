# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20161214_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_time', models.DateField(verbose_name='\u4e0a\u8bfe\u65f6\u95f4')),
                ('course', models.ForeignKey(related_name='teach_course_course', verbose_name='\u8bfe\u7a0b', to='index.Course')),
                ('teacher', models.ForeignKey(related_name='teach_course_teacher', verbose_name='\u5916\u6559', to='index.Teacher')),
            ],
            options={
                'ordering': ['course_time'],
                'verbose_name': '\u5916\u6559\u4e0a\u8bfe\u8868',
                'db_table': 't_teachcourse',
                'managed': True,
                'verbose_name_plural': '\u5916\u6559\u4e0a\u8bfe\u8868',
            },
        ),
    ]
