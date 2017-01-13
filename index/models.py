# coding: utf-8
from django.db import models


SEX_CHOICES = ((0, u'女'), (1, u'男'),)
DOC_TYPE_CHOICES = ((0, u'复习'), (1, u'预习'), (1, u'作业'))
CONSTELLATION_CHOICES = ((0, u'白羊座'), (1, u'金牛座'), (2, u'双子座'), (3, u'巨蟹座'), (4, u'狮子座'), (5, u'处女座'),
                         (6, u'天秤座'), (7, u'天蝎座'), (8, u'射手座'), (9, u'摩羯座'), (10, u'水瓶座'), (11, u'双鱼座'), )
PAY_WAY_CHOICES =((0, u'12月分期付款，每月的金额'), (1, u'一次性付清'),)
USED_STATE_CHOICES = ((0, u'未使用'), (1, u'已使用'), (2, u'已过期'),)
SHORT_MESSAGE_CHOICES = ((0, u'提醒'), (1, u'不提醒'),)
AUTO_SUBSTITUTE_CHOICES = ((0, u'启动'), (0, u'关闭'),)
STUDY_RECORD_STATE_CHOICES = ((0, u'已上完'), (1, u'未上'), (2, u'未上完'),)
CURRENT_ENGLISH_LV_CHOICES = ((0, u'零基础'), (1, u'L1'), (2, u'L2'), (3, u'L3'), (4, u'L4'), (5, u'L5'), (6, u'L6'), (7, u'L7'),
                              (8, u'L8'), (9, u'L9'), (10, u'L10'), (11, u'L11'), (12, u'L12'),)
SCORES_CHOICES = ((0, u'1分'), (1, u'2分'), (2, u'3分'), (3, u'4分'), (4, u'5分'),)
ORDER_STATE_CHOICES = ((0, u'已付款'), (1, u'未付款'),)

YES_NO_CHOICES = ((0,u'是'), (1, u'否'),)
INTEREST_CHOICES = ((0, u'不感兴趣'), (1, u'一般'), (2, u'感兴趣'), )
DIFFICULT_CHOICES = ((0, u'太难'), (1, u'太简单'), (2, u'适中'), )
TOOL_CLASS_CHOICES = ((0, u'用专用软件'), (1, u'使用Skype上课'), (2, u'使用qq上课'),)
INTRODUCTION_CHOICES = ((0, u'不需要外教和我双方做任何自我介绍'), (1, u'简短即可控制在2分钟内'), )
ERROR_CORRECTION_WAY_CHOICES = ((0, u'在上课过程中适度适时纠错'), (1, u'当我出现使用错误时外教立即纠错，有错即纠正'), )
FINISH_CHOICES = ((0, u'未完成'), (1, u'已完成'), )
COMPLAIN_REASON_CHOICES = ((0, u'关于外教'), (1, u'关于教材'), (2, u'关于网站'), (3, u'关于客户端'), (4, u'关于顾客/客服'), (5, u'其他'), )
SHARE_PLATFORM_CHOICES = ((0, u'qq'),(1, u'微信'), (2, u'微博'), )
MAJOR_CHOICES = ((0, u'医疗卫生'), (1, u'IT/电子/通信'), (2, u'经济/金融'), (3, u'餐饮旅游'), (4, u'文化传媒'), (5, u'营销/公关'),
                 (6, u'教育/培训'), (7, u'人力资源'), (8, u'政府/社会服务'), (9, u'高科技产业'), (10, u'制造业'), (11, u'建筑/设计'),
                 (12, u'学术/科研'), (13, u'法律'), (14, u'航空/航天'), (15, u'零售/批发'), (16, u'咨询服务'), (17, u'外贸/进出口'),
                 (18, u'运输物流'), (19, u'印刷/出版'), (20, u'能源产业'), (21, u'其他'), )
LV_CHOICES = ((0, u'零基础'), (1, u'Lv1'), (2, u'Lv2'), (3, u'Lv3'), (4, u'Lv4'), (5, u'Lv5'), (6, u'Lv6'), (7, u'Lv7'), (8, u'Lv8'),
              (9, u'Lv9'), (10, u'Lv10'),  (11, u'Lv11'), (12, u'Lv12'), (13, u'Lv13'), (14, u'Lv14'), (15, u'Lv15'), (16, u'Lv16'), )
# Create your models here
class FrontPageSlider(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=100)
    description = models.CharField(verbose_name=u'描述', max_length=300)
    images = models.ImageField(verbose_name=u'图片', upload_to='static/images', default='')
    url = models.URLField(verbose_name=u'链接')
    action = models.CharField(verbose_name=u'操作', max_length=10, default='')

    def __unicode__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["title"]
        db_table = 't_frontpagelider'
        verbose_name = u'首页幻灯片'
        verbose_name_plural = u'首页幻灯片'

class ComboType(models.Model):
    combo_name = models.CharField(verbose_name=u'类型名', max_length=100)
    user = models.CharField(verbose_name=u'适用的学生', max_length=300)
    advantage = models.CharField(verbose_name=u'优势', max_length=1000)
    note = models.CharField(verbose_name=u'注意', max_length=1000)

    def __unicode__(self): # python编码
        return self.combo_name

    class Meta:
        managed = True
        app_label = 'index' # 所处的文件夹
        ordering = ['combo_name'] # 按照那个属性进行排序
        db_table = 't_combotype' # 表名（数据库中的）
        verbose_name = u'套餐类型表' # 给自己看的表名（在后台吧）
        verbose_name_plural = u'套餐类型表'

#  一对多的关系,related_name是用来反向查询的，不写，则默认是foo_set(foo是关联表的表名小写)
class CountCombo(models.Model):
    combo_type = models.ForeignKey(ComboType, verbose_name=u'所属的类型')
    count_name = models.CharField(verbose_name=u'次卡数名字', max_length=50)
    count_number = models.PositiveIntegerField(verbose_name=u'次卡数量')
    public_number = models.PositiveIntegerField(verbose_name=u'优选公开课的数量')
    unit = models.CharField(verbose_name=u'课的单位，默认为课时', default='课时', max_length=8)
    valid_date = models.PositiveIntegerField(verbose_name=u'有效期')
    money = models.PositiveIntegerField(verbose_name=u'金额')
    italk_used = models.PositiveIntegerField(verbose_name=u'italk免费使用权数', blank=True, null=True)
    italk_used_unit = models.CharField(verbose_name=u'italk免费使用权的单位', default='月', max_length=10, blank=True)
    present_course = models.PositiveIntegerField(verbose_name=u'赠送课程数', blank=True, null=True)
    present_course_unit = models.CharField(verbose_name=u'赠送课程数的单位', default='节', max_length=10, blank=True)

    def __unicode__(self):
        return self.count_name

    class Meta:
        managed = True
        app_label = 'index' # 所处的文件夹
        ordering = ['count_name'] # 按照那个属性进行排序
        db_table = 't_countcombo' # 表名（数据库中的）
        verbose_name = u'次卡套餐' # 给自己看的表名（在后台吧）
        verbose_name_plural = u'次卡套餐'

class MonthCombo(models.Model):
    combo_type = models.ForeignKey(ComboType, verbose_name=u'所属的类型')
    month_name = models.CharField(verbose_name=u'包月套餐的名字', max_length=100)
    month_number = models.PositiveIntegerField(verbose_name=u'包月数量')
    valid_date = models.PositiveIntegerField(verbose_name=u'有效期')
    money = models.PositiveIntegerField(verbose_name=u'金额')
    italk_used = models.PositiveIntegerField(verbose_name=u'italk免费使用权数', blank=True, null=True)
    italk_used_unit = models.CharField(verbose_name=u'italk免费使用权的单位', default='月', max_length=10, blank=True)
    present_course = models.PositiveIntegerField(verbose_name=u'赠送课程数',  blank=True, null=True)
    present_course_unit = models.CharField(verbose_name=u'赠送课程数的单位', default='节', max_length=10, blank=True)

    def __unicode__(self):
        return self.month_name

    class Meta:
        managed = True
        app_label = 'index' # 所处的文件夹
        ordering = ['month_name'] # 按照那个属性进行排序
        db_table = 't_monthcombo' # 表名（数据库中的）
        verbose_name = u'包月套餐' # 给自己看的表名（在后台吧）
        verbose_name_plural = u'包月套餐'

# class DocType(models.Model):
#     type_name = models.PositiveIntegerField(verbose_name=u'文档类型名', default=0, choices=DOC_TYPE_CHOICES)
#
#     def __unicode__(self):  # __unicode__ on Python 2
#         return str(self.id)
#
#     class Meta:
#         managed = True
#         app_label = 'index'
#         ordering = ["type_name"]
#         db_table = 't_doctype'
#         verbose_name = u'文档类型表'
#         verbose_name_plural = u'文档类型表'

class MainCategory(models.Model):
    main_name = models.CharField(verbose_name=u'主分类名', max_length=20)

    def main_category_title(self):
        return self.main_name

    def __unicode__(self):
        return self.main_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_maincategory'
        verbose_name = u'课程主分类表'
        verbose_name_plural = u'课程主分类表'

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, verbose_name=u'主分类名', default=0)
    sub_name = models.CharField(verbose_name=u'次分类名', max_length=20)

    def sub_category_name(self):
        return self.sub_name

    def __unicode__(self):
        return '%s:%s' % (self.main_category.main_name, self.sub_name)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_subcategory'
        verbose_name = u'课程次分类表'
        verbose_name_plural = u'课程次分类表'

class SmallCategory(models.Model):
    main_sub_category = models.ForeignKey(SubCategory, verbose_name=u'主与次分类', default=0)
    small_name = models.CharField(verbose_name= u'小分类名', max_length=20)

    def __unicode__(self):
        return '%s:%s:%s' % (self.main_sub_category.main_category.main_name, self.main_sub_category.sub_name, self.small_name)

    def small_category_name(self):
        return self.small_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_smallcategory'
        verbose_name = u'课程小分类表'
        verbose_name_plural = u'课程小分类表'

# class DetailCategory(models.Model):
#     main_category = models.ForeignKey(MainCategory, verbose_name=u'主分类名')
#     sub_category = models.ForeignKey(SubCategory, verbose_name=u'次分类名')
#     small_category = models.ForeignKey(SmallCategory, verbose_name=u'小分类名')
#
#     def sub_category_id(self):
#         return self.sub_category_id
#
#     def sub_category_title(self):
#         return self.sub_category.sub_name
#
#     def __unicode__(self):
#         return str(self.id)
#
#     class Meta:
#         managed = True
#         app_label = 'index'
#         ordering = ["id"]
#         db_table = 't_detailcategory'
#         verbose_name = u'课程详细分类'
#         verbose_name_plural = u'课程详细分类'
class Unit(models.Model):
    unit_name = models.CharField(verbose_name=u'单位名', max_length=20)

    def __unicode__(self):
        return self.unit_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_unit'
        verbose_name = u'单位表'
        verbose_name_plural = u'单位表'

class Course(models.Model):
    course_name = models.CharField(verbose_name=u'课程名', max_length=100)
    image = models.ImageField(verbose_name=u'课程图片', upload_to='static/images', default='')
    target = models.CharField(verbose_name=u'课程预计目标', max_length=100)
    course_number = models.PositiveIntegerField(verbose_name=u'课程数', default=0)
    course_unit = models.ForeignKey(Unit, verbose_name=u'课程单位', related_name='course_course_unit', blank=True, default=0)
    pay_number = models.PositiveIntegerField(verbose_name=u'付款数',default=0)
    pay_unit = models.ForeignKey(Unit, verbose_name=u'付款单位', related_name='course_pay_unit', blank=True, default=0)
    student_lv_low = models.PositiveIntegerField(verbose_name=u'适合学员水平1', default=0, choices=LV_CHOICES)
    student_lv_height = models.PositiveIntegerField(verbose_name=u'适合学员水平2', default=0, choices=LV_CHOICES)
    description = models.TextField(verbose_name=u'课程描述', max_length=100000)

    def __unicode__(self):   # __unicode__ on Python 2
        return self.course_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_course'
        verbose_name = u'课程表'
        verbose_name_plural = u'课程表'

class CourseCategory(models.Model):
    small_category = models.ForeignKey(SmallCategory, verbose_name=u'详细分类', default=0)
    course = models.ForeignKey(Course, verbose_name=u'课程')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_coursecategory'
        verbose_name = u'课程分类表'
        verbose_name_plural = u'课程分类表'

# class CourseType(models.Model):
#     type_name = models.CharField(verbose_name=u'课程类型名', max_length=100)
#
#     def __unicode__(self):   # __unicode__ on Python 2
#         return self.type_name
#
#     class Meta:
#         managed = True
#         app_label = 'index'
#         ordering = ["type_name"]
#         db_table = 't_coursetype'
#         verbose_name = u'课程类型表'
#         verbose_name_plural = u'课程类型表'

class DocSite(models.Model):
    type_name = models.PositiveIntegerField(verbose_name=u'文档类型名', default=0, choices=DOC_TYPE_CHOICES)
    # type = models.ForeignKey(DocType, verbose_name=u'文档类型', related_name='doc_type')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    doc_name = models.CharField(verbose_name=u'文档名', max_length=100)
    content = models.FileField(verbose_name=u'文档内容', upload_to='static/doc')

    def __unicode__(self):
        return self.doc_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["doc_name"]
        db_table = 't_doc'
        verbose_name = u'文档表'
        verbose_name_plural = u'文档表'

class Book(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    book_name = models.CharField(verbose_name=u'教材名字', max_length=100)
    description = models.CharField(verbose_name=u'教材描述', max_length=300)
    money = models.PositiveIntegerField(verbose_name=u'金额')
    special = models.CharField(verbose_name=u'教材特色', max_length=500)

    def __unicode__(self):   # __unicode__ on Python 2
        return self.book_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["book_name"]
        db_table = 't_book'
        verbose_name = u'教材'
        verbose_name_plural = u'教材'

class Teacher(models.Model):
    teacher_name = models.CharField(verbose_name=u'外教名', max_length=100)
    picture = models.ImageField(verbose_name=u'头像', upload_to='static/images')
    motto = models.CharField(verbose_name=u'铭言', max_length=300)
    be_good_at_course = models.CharField(verbose_name=u'擅长的课程', max_length=100)
    student_lv = models.CharField(verbose_name=u'适合学员', max_length=100)
    teacher_experience = models.CharField(verbose_name=u'教学经验', max_length=100)
    hobby = models.CharField(verbose_name=u'兴趣爱好', max_length=300)
    constellation = models.PositiveIntegerField(verbose_name=u'星座', default=0, choices=CONSTELLATION_CHOICES)
    major = models.PositiveIntegerField(verbose_name=u'大学专业', default=0, choices=MAJOR_CHOICES)
    work_industry = models.CharField(verbose_name=u'工作行业', max_length=100)
    star_number = models.FloatField(verbose_name=u'星星数')
    flowers_number = models.PositiveIntegerField(verbose_name=u'献花数')
    shared_number = models.PositiveIntegerField(verbose_name=u'分享数')
    introduction = models.CharField(verbose_name=u'自我介绍', max_length=500)
    dynamic = models.CharField(verbose_name=u'外教动态', max_length=1000, blank=True)

    def __unicode__(self):
        return self.teacher_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["teacher_experience"]
        db_table = 't_teacher'
        verbose_name = u'外教'
        verbose_name_plural = u'外教'

class Student(models.Model):
    # student_id = models.CharField(verbose_name=u'学号', max_length=20, unique=True)
    lv = models.PositiveIntegerField(verbose_name=u'英语水平',null=True,blank=True)
    study_number = models.PositiveIntegerField(verbose_name=u'学豆数量',default=0, null=True, blank=True)
    card_number = models.PositiveIntegerField(verbose_name=u'剩余次卡数',default=0, null=True, blank=True)
    english_name = models.CharField(verbose_name=u'英文名字', max_length=50,default='Student',null=True, blank=True)
    true_name = models.CharField(verbose_name=u'真实姓名', max_length=50, null=True, blank=True)
    mobile = models.CharField(verbose_name=u'手机', max_length=11)
    password = models.CharField(verbose_name=u'登录密码', max_length=20, default='11111111')
    picture = models.ImageField(verbose_name=u'头像', upload_to='static/images',null=True, blank=True)
    sex = models.PositiveIntegerField(verbose_name=u'性别',default=0, choices=SEX_CHOICES)
    qq = models.CharField(verbose_name=u'QQ', max_length=20,null=True, blank=True)
    birthday = models.DateField(verbose_name=u'生日',null=True,blank=True)
    recepient = models.CharField(verbose_name=u'收件人的姓名', max_length=50, null=True, blank=True)
    post_code = models.CharField(verbose_name=u'邮编', max_length=10,null=True, blank=True)
    address = models.CharField(verbose_name=u'收件人的地址', max_length=100,null=True, blank=True)
    target = models.PositiveIntegerField(verbose_name=u'目标级别', default=0, blank=True,null=True)
    need_number_target =models.PositiveIntegerField(verbose_name=u'距离升级还需要的节数', default=0, blank=True)
    week_target = models.PositiveIntegerField(verbose_name=u'周目标', default=0, blank=True)
    finish_week_target = models.PositiveIntegerField(verbose_name=u'完成的周节数', default=0, blank=True)
    finish_one_to_one_foreign = models.PositiveIntegerField(verbose_name=u'完成1对1外教课数', default=0, blank=True )
    total_time_talk_english = models.PositiveIntegerField(verbose_name=u'累计说英语数', default=0, blank=True,)
    recomment_mobile = models.CharField(verbose_name=u'推荐人的手机号',max_length=11,default='')
    is_apply_course = models.PositiveIntegerField(verbose_name=u'是否预约课程', default=1,choices=YES_NO_CHOICES)

    def __unicode__(self):
        return self.english_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_student'
        verbose_name = u'学员表'
        verbose_name_plural = u'学员表'

class StudentCollectTeacher(models.Model):
    student = models.ForeignKey(Student, verbose_name=u'学生')
    teacher = models.ForeignKey(Teacher, verbose_name=u'外教')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_studentcollectteacher'
        verbose_name = u'学生收藏外教'
        verbose_name_plural = u'学生收藏外教'

class StudentShareTeacher(models.Model):
    student = models.ForeignKey(Student, verbose_name=u'学生')
    teacher = models.ForeignKey(Teacher, verbose_name=u'外教')
    share_platform = models.PositiveIntegerField(verbose_name=u'分享平台', default=0, choices=SHARE_PLATFORM_CHOICES)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["id"]
        db_table = 't_studentshareteacher'
        verbose_name_plural = u'学生分享外教'
        verbose_name = u'学生分享外教'

class Favourable(models.Model):
        favourable_id = models.CharField(verbose_name=u'优惠编号', max_length=10)
        favourable_money = models.PositiveIntegerField(verbose_name=u'优惠金额')
        favourable_description =models.CharField(verbose_name=u'优惠描述', max_length=300)

        def __unicode__(self):
            return self.favourable_id

        class Meta:
            managed = True
            app_label = 'index'
            ordering =["favourable_money"]
            db_table = 't_favourable'
            verbose_name = u'优惠表'
            verbose_name_plural = u'优惠表'

class FavourableProduct(models.Model):
    product_name = models.CharField(verbose_name=u'优惠产品名', max_length=100)
    product_price = models.PositiveIntegerField(verbose_name=u'优惠价格')

    def __unicode__(self):
        return self.product_name

    class Meta:
        managed = True
        app_label = 'index'
        ordering =["product_price"]
        db_table = 't_favourableproduct'
        verbose_name = u'优惠产品表'
        verbose_name_plural = u'优惠产品表'

class PayWay(models.Model):
    pay_way_type = models.PositiveIntegerField(verbose_name=u'收费方式', default=0, choices=PAY_WAY_CHOICES)
    pay_platform = models.CharField(verbose_name=u'收费平台', max_length=300)

    def __unicode__(self):
        return self.pay_platform

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["pay_way_type"]
        db_table = 't_payway'
        verbose_name = u'付费方式表'
        verbose_name_plural = u'付费方式表'

class Coupon(models.Model):
    coupon_id = models.CharField(verbose_name=u'代金券的编号', max_length=10)
    coupon_money = models.PositiveIntegerField(verbose_name=u'代金券的金额')
    valid_date = models.DateField(verbose_name=u'有效期')
    state =models.PositiveIntegerField(verbose_name=u'代金券的状态', default=0, choices=USED_STATE_CHOICES)

    def __unicode__(self):
        return self.coupon_id

    class Meta:
        managed = True
        app_label = 'index'
        ordering =["coupon_money"]
        db_table = 't_coupon'
        verbose_name = u'代金券'
        verbose_name_plural = u'代金券'

class Setting(models.Model):
    student = models.OneToOneField(Student, verbose_name=u'学生', default='')
    short_message = models.PositiveIntegerField(verbose_name=u'短信提醒', default=0, choices=SHORT_MESSAGE_CHOICES)
    auto_substitute = models.PositiveIntegerField(verbose_name=u'系统自动代理', default=0, choices=AUTO_SUBSTITUTE_CHOICES)

    def __unicode__(self):
        return str(self.student)  #  __unicode__()方法，方法告诉Python如何将对象以unicode的方式显示出来，唯一的要求就是：它要返回一个unicode对象 如果`` __unicode__()`` 方法未返回一个Unicode对象，而返回比如说一个整型数字，那么Python将抛出一个`` TypeError`` 错误，并提示：”coercing to Unicode: need string or buffer, int found”

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["short_message"]
        db_table = 't_setting'
        verbose_name = u'上课设置表'
        verbose_name_plural = u'上课设置表'

class TeachCourse(models.Model):
    course_time = models.DateTimeField(verbose_name=u'上课时间')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    teacher = models.ForeignKey(Teacher, verbose_name=u'外教')

    def __unicode__(self):
        return str(self.course_time)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["course_time"]
        db_table = 't_teachcourse'
        verbose_name = u'外教上课表'
        verbose_name_plural = u'外教上课表'

class ReceiveCoupon(models.Model):
    coupon = models.ForeignKey(Coupon, verbose_name=u'代金券')
    student = models.ForeignKey(Student, verbose_name=u'学员')
    receive_time = models.DateTimeField(verbose_name=u'领取时间')

    def __unicode__(self):
        return str(self.coupon)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["receive_time"]
        db_table = 't_receivecoupon'
        verbose_name = u'领取代金券'
        verbose_name_plural = u'领取代金券'

class StudyRecord(models.Model):
    student = models.ForeignKey(Student, verbose_name=u'学员')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    state = models.PositiveIntegerField(verbose_name=u'状态', default=0, choices=STUDY_RECORD_STATE_CHOICES)
    tool_class = models.PositiveIntegerField(verbose_name=u'上课工具', default=0, choices=TOOL_CLASS_CHOICES)
    introduction = models.PositiveIntegerField(verbose_name=u'自我介绍', default=0, choices=INTRODUCTION_CHOICES)
    error_correction_way = models.PositiveIntegerField(verbose_name=u'纠错方式', default=0, choices=ERROR_CORRECTION_WAY_CHOICES)
    leave_a_message = models.TextField(verbose_name=u'给外教留言', default='')
    preparation = models.PositiveIntegerField(verbose_name=u'课前预习', default=0, choices=FINISH_CHOICES)
    review = models.PositiveIntegerField(verbose_name=u'课后复习', default=0, choices=FINISH_CHOICES)
    homework = models.PositiveIntegerField(verbose_name=u'课后作业', default=0, choices=FINISH_CHOICES)
    cancel = models.PositiveIntegerField(verbose_name=u'取消课程', default=0, choices=YES_NO_CHOICES)
    flowers = models.PositiveIntegerField(verbose_name=u'献花数', default=0)
    chatting_record = models.FileField(verbose_name=u'聊天记录', upload_to='static/doc', default='')

    def __unicode__(self):
        return str(self.student)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["state"]
        db_table = 't_studyrecord'
        verbose_name = u'上课记录'
        verbose_name_plural = u'上课记录'

class Complain(models.Model):
    study_record = models.ForeignKey(StudyRecord, verbose_name=u'上课记录')
    complain_reason = models.PositiveIntegerField(verbose_name=u'投诉类型', default=0, choices=COMPLAIN_REASON_CHOICES)
    complain_content = models.TextField(verbose_name=u'投诉内容')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["complain_reason"]
        db_table = 't_complain'
        verbose_name= u'投诉表'
        verbose_name_plural =  u'投诉表'

class ReviseCourse(models.Model):
      study_record = models.OneToOneField(StudyRecord, verbose_name=u'上课记录')
      class_doc = models.FileField(verbose_name=u'上课资料', upload_to='static/doc')

      def __unicode__(self):
          return str(self.id)

      class Meta:
          managed = True
          app_label = 'index'
          ordering = ["id"]
          db_table = 't_revisecourse'
          verbose_name_plural = u'修改课程'
          verbose_name = u'修改课程'


class TeacherEvaluate(models.Model):
    study_record = models.OneToOneField(StudyRecord, verbose_name=u'上课记录')
    current_lv = models.PositiveIntegerField(verbose_name=u'当前英语水平', default=0, choices=CURRENT_ENGLISH_LV_CHOICES)
    pronunication = models.PositiveIntegerField(verbose_name=u'发音分数',default=0, choices=SCORES_CHOICES)
    grammar = models.PositiveIntegerField(verbose_name=u'语法分数', default=0, choices=SCORES_CHOICES)
    vocabulary = models.PositiveIntegerField(verbose_name=u'词汇分数', default=0, choices=SCORES_CHOICES)
    fluency = models.PositiveIntegerField(verbose_name=u'流利度分数', default=0, choices=SCORES_CHOICES)
    listening = models.PositiveIntegerField(verbose_name=u'听力理解分数', default=0, choices=SCORES_CHOICES)
    performance = models.CharField(verbose_name=u'课程表现', max_length=100)
    grammar_or_sentence = models.CharField(verbose_name=u'语法/句型', max_length=500)
    pronunication_vocabulary = models.CharField(verbose_name=u'发音单词', max_length=500)

    def __unicode__(self):
        return self.performance

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["current_lv"]
        db_table = 't_teacherevaluate'
        verbose_name = u'外教评价表'
        verbose_name_plural = u'外教评价表'

class StudentEvaluate(models.Model):
    study_record = models.OneToOneField(StudyRecord, verbose_name=u'上课记录')
    on_time_class = models.PositiveIntegerField(verbose_name=u'外教按时上课', default=0, choices=YES_NO_CHOICES)
    active_video = models.PositiveIntegerField(verbose_name=u'外教主动视频', default=0, choices=YES_NO_CHOICES)
    network = models.PositiveIntegerField(verbose_name=u'外教网络效果（星星数）', default=0)
    pronunication_standard = models.PositiveIntegerField(verbose_name=u'外教发音标准（星星数）', default=0)
    broaden_knowledge = models.PositiveIntegerField(verbose_name=u'知识拓展与纠错（星星数）', default=0)
    attitute = models.PositiveIntegerField(verbose_name=u'态度好耐心引导', default=0)
    tag = models.CharField(verbose_name=u'给外教打标签', max_length=1000)
    teacher_content = models.TextField(verbose_name=u'对外教的评语', blank=True)
    book_quality = models.PositiveIntegerField(verbose_name=u'教材的品质（星星数）', default=0)
    book_interest = models.PositiveIntegerField(verbose_name=u'对教材的兴趣',default=0, choices=INTEREST_CHOICES)
    book_difficult = models.PositiveIntegerField(verbose_name=u'教材的难度', default=0, choices=DIFFICULT_CHOICES)
    book_content = models.TextField(verbose_name=u'对教材的评语', blank=True)
    time = models.DateTimeField(verbose_name=u'学生评价时间')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["time"]
        db_table = 't_studentevaluate'
        verbose_name = u'学员评价'
        verbose_name_plural = u'学员评价'

class AgainStudyApply(models.Model):
    study_record = models.OneToOneField(StudyRecord, verbose_name=u'上课记录')
    reason = models.CharField(verbose_name=u'申请理由', max_length=1000)

    def __unicode__(self):
        return self.reason

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["reason"]
        db_table = 't_againstudyapply'
        verbose_name = u'申请重新上课'
        verbose_name_plural = u'申请重新上课'

class Order(models.Model):
    order_id = models.CharField(verbose_name=u'订单号', max_length=100)
    favourable_money = models.PositiveIntegerField(verbose_name=u'优惠金额')
    capital = models.PositiveIntegerField(verbose_name=u'实付金额')
    pay_time = models.DateTimeField(verbose_name=u'付款时间')
    state = models.PositiveIntegerField(verbose_name=u'状态', default=0, choices=ORDER_STATE_CHOICES)
    bill = models.FileField(verbose_name=u'发票',upload_to='static/doc')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["pay_time"]
        verbose_name = u'订单'
        verbose_name_plural = u'订单'

class OrderDetail(models.Model):
    count_combo = models.ManyToManyField(CountCombo, verbose_name=u'次卡套餐')
    month_combo = models.ManyToManyField(MonthCombo, verbose_name=u'包月套餐')
    pay_way = models.ForeignKey(PayWay, verbose_name=u'付款方式')
    favourable_product = models.ManyToManyField(FavourableProduct, verbose_name=u'优惠产品')
    order = models.OneToOneField(Order, verbose_name=u'订单')
    coupon = models.ManyToManyField(ReceiveCoupon, verbose_name=u'领取代金券')
    quantity = models.PositiveIntegerField(verbose_name=u'数量')

    def __unicode__(self):
        return str(self.quantity)


    class Meta:
        managed = True
        app_label = 'index'
        ordering = ["quantity"]
        verbose_name = u'订单详细'
        verbose_name_plural = u'订单详细'

class ShoppingCar(models.Model):
     count_combo = models.ManyToManyField(CountCombo, verbose_name=u'次卡套餐', blank=True)
     month_combo = models.ManyToManyField(MonthCombo, verbose_name=u'包月套餐', blank=True)
     student = models.OneToOneField(Student, verbose_name=u'学员')

     def __unicode__(self):
         return str(self.id)

     class Meta:
        managed = True
        app_label = 'index'
        ordering = ["student"]
        verbose_name = u'购物车'
        verbose_name_plural = u'购物车'


