# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0023_auto_20161217_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complain_reason', models.PositiveIntegerField(default=0, verbose_name='\u6295\u8bc9\u7c7b\u578b', choices=[(0, '\u5173\u4e8e\u5916\u6559'), (1, '\u5173\u4e8e\u6559\u6750'), (2, '\u5173\u4e8e\u7f51\u7ad9'), (3, '\u5173\u4e8e\u5ba2\u6237\u7aef'), (4, '\u5173\u4e8e\u987e\u5ba2/\u5ba2\u670d'), (5, '\u5176\u4ed6')])),
                ('complain_content', models.TextField(verbose_name='\u6295\u8bc9\u5185\u5bb9')),
            ],
            options={
                'ordering': ['complain_reason'],
                'verbose_name': '\u6295\u8bc9\u8868',
                'db_table': 't_complain',
                'managed': True,
                'verbose_name_plural': '\u6295\u8bc9\u8868',
            },
        ),
        migrations.CreateModel(
            name='ReviseCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_doc', models.FileField(upload_to=b'static/doc', verbose_name='\u4e0a\u8bfe\u8d44\u6599')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u4fee\u6539\u8bfe\u7a0b',
                'db_table': 't_revisecourse',
                'managed': True,
                'verbose_name_plural': '\u4fee\u6539\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='StudentCollectTeacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5b66\u751f\u6536\u85cf\u5916\u6559',
                'db_table': 't_studentcollectteacher',
                'managed': True,
                'verbose_name_plural': '\u5b66\u751f\u6536\u85cf\u5916\u6559',
            },
        ),
        migrations.CreateModel(
            name='StudentShareTeacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share_platform', models.PositiveIntegerField(default=0, verbose_name='\u5206\u4eab\u5e73\u53f0', choices=[(0, 'qq'), (1, '\u5fae\u4fe1'), (2, '\u5fae\u535a')])),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5b66\u751f\u5206\u4eab\u5916\u6559',
                'db_table': 't_studentshareteacher',
                'managed': True,
                'verbose_name_plural': '\u5b66\u751f\u5206\u4eab\u5916\u6559',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='finish_one_to_one_foreign',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5b8c\u62101\u5bf91\u5916\u6559\u8bfe\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='finish_week_target',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5b8c\u6210\u7684\u5468\u8282\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='need_number_target',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8ddd\u79bb\u5347\u7ea7\u8fd8\u9700\u8981\u7684\u8282\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='target',
            field=models.PositiveIntegerField(default=0, verbose_name='\u76ee\u6807\u7ea7\u522b', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='total_time_talk_english',
            field=models.PositiveIntegerField(default=0, verbose_name='\u7d2f\u8ba1\u8bf4\u82f1\u8bed\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='week_target',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5468\u76ee\u6807', blank=True),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='cancel',
            field=models.PositiveIntegerField(default=0, verbose_name='\u53d6\u6d88\u8bfe\u7a0b', choices=[(0, '\u662f'), (1, '\u5426')]),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='chatting_record',
            field=models.FileField(default=b'', upload_to=b'static/doc', verbose_name='\u804a\u5929\u8bb0\u5f55'),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='error_correction_way',
            field=models.PositiveIntegerField(default=0, verbose_name='\u7ea0\u9519\u65b9\u5f0f', choices=[(0, '\u5728\u4e0a\u8bfe\u8fc7\u7a0b\u4e2d\u9002\u5ea6\u9002\u65f6\u7ea0\u9519'), (1, '\u5f53\u6211\u51fa\u73b0\u4f7f\u7528\u9519\u8bef\u65f6\u5916\u6559\u7acb\u5373\u7ea0\u9519\uff0c\u6709\u9519\u5373\u7ea0\u6b63')]),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='flowers',
            field=models.PositiveIntegerField(default=0, verbose_name='\u732e\u82b1\u6570'),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='homework',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8bfe\u540e\u4f5c\u4e1a', choices=[(0, '\u672a\u5b8c\u6210'), (1, '\u5df2\u5b8c\u6210')]),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='introduction',
            field=models.PositiveIntegerField(default=0, verbose_name='\u81ea\u6211\u4ecb\u7ecd', choices=[(0, '\u4e0d\u9700\u8981\u5916\u6559\u548c\u6211\u53cc\u65b9\u505a\u4efb\u4f55\u81ea\u6211\u4ecb\u7ecd'), (1, '\u7b80\u77ed\u5373\u53ef\u63a7\u5236\u57282\u5206\u949f\u5185')]),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='leave_a_message',
            field=models.TextField(default=b'', verbose_name='\u7ed9\u5916\u6559\u7559\u8a00'),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='preparation',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8bfe\u524d\u9884\u4e60', choices=[(0, '\u672a\u5b8c\u6210'), (1, '\u5df2\u5b8c\u6210')]),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='review',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8bfe\u540e\u590d\u4e60', choices=[(0, '\u672a\u5b8c\u6210'), (1, '\u5df2\u5b8c\u6210')]),
        ),
        migrations.AddField(
            model_name='studyrecord',
            name='tool_class',
            field=models.PositiveIntegerField(default=0, verbose_name='\u4e0a\u8bfe\u5de5\u5177', choices=[(0, '\u7528\u4e13\u7528\u8f6f\u4ef6'), (1, '\u4f7f\u7528Skype\u4e0a\u8bfe'), (2, '\u4f7f\u7528qq\u4e0a\u8bfe')]),
        ),
        migrations.AlterField(
            model_name='docsite',
            name='type_name',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6587\u6863\u7c7b\u578b\u540d', choices=[(0, '\u590d\u4e60'), (1, '\u9884\u4e60'), (1, '\u4f5c\u4e1a')]),
        ),
        migrations.AlterField(
            model_name='studentevaluate',
            name='tag',
            field=models.CharField(max_length=1000, verbose_name='\u7ed9\u5916\u6559\u6253\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='major',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5927\u5b66\u4e13\u4e1a', choices=[(0, '\u533b\u7597\u536b\u751f'), (1, 'IT/\u7535\u5b50/\u901a\u4fe1'), (2, '\u7ecf\u6d4e/\u91d1\u878d'), (3, '\u9910\u996e\u65c5\u6e38'), (4, '\u6587\u5316\u4f20\u5a92'), (5, '\u8425\u9500/\u516c\u5173'), (6, '\u6559\u80b2/\u57f9\u8bad'), (7, '\u4eba\u529b\u8d44\u6e90'), (8, '\u653f\u5e9c/\u793e\u4f1a\u670d\u52a1'), (9, '\u9ad8\u79d1\u6280\u4ea7\u4e1a'), (10, '\u5236\u9020\u4e1a'), (11, '\u5efa\u7b51/\u8bbe\u8ba1'), (12, '\u5b66\u672f/\u79d1\u7814'), (13, '\u6cd5\u5f8b'), (14, '\u822a\u7a7a/\u822a\u5929'), (15, '\u96f6\u552e/\u6279\u53d1'), (16, '\u54a8\u8be2\u670d\u52a1'), (17, '\u5916\u8d38/\u8fdb\u51fa\u53e3'), (18, '\u8fd0\u8f93\u7269\u6d41'), (19, '\u5370\u5237/\u51fa\u7248'), (20, '\u80fd\u6e90\u4ea7\u4e1a'), (21, '\u5176\u4ed6')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='student_lv',
            field=models.CharField(max_length=100, verbose_name='\u9002\u5408\u5b66\u5458'),
        ),
        migrations.AddField(
            model_name='studentshareteacher',
            name='student',
            field=models.ForeignKey(related_name='student_share', verbose_name='\u5b66\u751f', to='index.Student'),
        ),
        migrations.AddField(
            model_name='studentshareteacher',
            name='teacher',
            field=models.ForeignKey(related_name='teacher_share', verbose_name='\u5916\u6559', to='index.Teacher'),
        ),
        migrations.AddField(
            model_name='studentcollectteacher',
            name='student',
            field=models.ForeignKey(related_name='student_collection', verbose_name='\u5b66\u751f', to='index.Student'),
        ),
        migrations.AddField(
            model_name='studentcollectteacher',
            name='teacher',
            field=models.ForeignKey(related_name='teacher_collection', verbose_name='\u5916\u6559', to='index.Teacher'),
        ),
        migrations.AddField(
            model_name='revisecourse',
            name='study_record',
            field=models.OneToOneField(related_name='revise_study_record', verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
        migrations.AddField(
            model_name='complain',
            name='study_record',
            field=models.ForeignKey(related_name='complain_study_record', verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
    ]
