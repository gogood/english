#-*-coding:UTF-8-*-
from django.db import models

# Create your models here.
class NoticeArticle(models.Model):

    CATEGORY_CHOICES=(
        (u'0', u'教务处通知'),
        (u'1', u'二级学院教学秘书通知')
    )

    title = models.CharField(max_length=60, verbose_name=u'标题')
    content = models.TextField(max_length=100000, verbose_name=u'正文')
    create_at = models.DateTimeField(verbose_name=u'发布时间')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name=u'分类')

    def __unicode__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 't_notifications'
        app_label = 'notifications_management'
        verbose_name = u'通知公告'
        verbose_name_plural = u'通知公告'