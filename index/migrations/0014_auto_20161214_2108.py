# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20161214_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgainStudyApply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=1000, verbose_name='\u7533\u8bf7\u7406\u7531')),
            ],
            options={
                'ordering': ['reason'],
                'verbose_name': '\u7533\u8bf7\u91cd\u65b0\u4e0a\u8bfe',
                'db_table': 't_againstudyapply',
                'managed': True,
                'verbose_name_plural': '\u7533\u8bf7\u91cd\u65b0\u4e0a\u8bfe',
            },
        ),
        migrations.CreateModel(
            name='ReceiveCoupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receive_time', models.DateTimeField(verbose_name='\u9886\u53d6\u65f6\u95f4')),
                ('note', models.CharField(default=b'', max_length=100, verbose_name='\u5907\u6ce8')),
                ('coupon', models.ForeignKey(related_name='receive_coupon', verbose_name='\u4ee3\u91d1\u5238', to='index.Coupon')),
                ('student', models.ForeignKey(related_name='receive_student', verbose_name='\u5b66\u5458', to='index.Student')),
            ],
            options={
                'ordering': ['receive_time'],
                'verbose_name': '\u9886\u53d6\u4ee3\u91d1\u5238',
                'db_table': 't_receivecoupon',
                'managed': True,
                'verbose_name_plural': '\u9886\u53d6\u4ee3\u91d1\u5238',
            },
        ),
        migrations.CreateModel(
            name='StudentEvaluate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluate_type', models.CharField(max_length=10, verbose_name='\u8bc4\u4ef7\u7c7b\u578b')),
                ('star_number', models.IntegerField(verbose_name='\u661f\u661f\u6570')),
                ('time', models.DateTimeField(verbose_name='\u5b66\u751f\u8bc4\u4ef7\u65f6\u95f4')),
                ('content', models.CharField(max_length=1000, verbose_name='\u8bc4\u4ef7\u5185\u5bb9')),
            ],
            options={
                'ordering': ['time'],
                'verbose_name': '\u5b66\u5458\u8bc4\u4ef7',
                'db_table': 't_studentevaluate',
                'managed': True,
                'verbose_name_plural': '\u5b66\u5458\u8bc4\u4ef7',
            },
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=10, verbose_name='\u72b6\u6001')),
                ('course', models.ForeignKey(related_name='student_record_course', verbose_name='\u8bfe\u7a0b', to='index.Course')),
                ('student', models.ForeignKey(related_name='student_record_student', verbose_name='\u5b66\u5458', to='index.Student')),
            ],
            options={
                'ordering': ['state'],
                'verbose_name': '\u4e0a\u8bfe\u8bb0\u5f55',
                'db_table': 't_studyrecord',
                'managed': True,
                'verbose_name_plural': '\u4e0a\u8bfe\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='TeacherEvaluate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_lv', models.IntegerField(verbose_name='\u5f53\u524d\u82f1\u8bed\u6c34\u5e73')),
                ('pronunication', models.IntegerField(verbose_name='\u53d1\u97f3\u5206\u6570')),
                ('grammar', models.IntegerField(verbose_name='\u8bed\u6cd5\u5206\u6570')),
                ('vocabulary', models.IntegerField(verbose_name='\u8bcd\u6c47\u5206\u6570')),
                ('fluency', models.IntegerField(verbose_name='\u6d41\u5229\u5ea6\u5206\u6570')),
                ('listening', models.IntegerField(verbose_name='\u542c\u529b\u7406\u89e3\u5206\u6570')),
                ('performance', models.CharField(max_length=100, verbose_name='\u8bfe\u7a0b\u8868\u73b0')),
                ('grammar_or_sentence', models.CharField(max_length=500, verbose_name='\u8bed\u6cd5/\u53e5\u578b')),
                ('pronunication_vocabulary', models.CharField(max_length=500, verbose_name='\u53d1\u97f3\u5355\u8bcd')),
                ('study_record', models.OneToOneField(related_name='teacher_study_record', verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord')),
            ],
            options={
                'ordering': ['current_lv'],
                'verbose_name': '\u5916\u6559\u8bc4\u4ef7\u8868',
                'db_table': 't_teacherevaluate',
                'managed': True,
                'verbose_name_plural': '\u5916\u6559\u8bc4\u4ef7\u8868',
            },
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='study_record',
            field=models.OneToOneField(related_name='student_study_record', verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
        migrations.AddField(
            model_name='againstudyapply',
            name='study_record',
            field=models.OneToOneField(related_name='again_study_record', verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
    ]
