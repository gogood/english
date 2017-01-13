# coding:utf-8
from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline, StackedInline
from nested_inline.admin import NestedModelAdmin
#from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from django_ueditor.widgets import UEditorWidget
from django import forms
from index.Inline import SubCategoryInline, SmallCategoryInline
from index.models import FrontPageSlider, ComboType, CountCombo, MonthCombo, Course, Book, DocSite, \
    Teacher, Favourable, FavourableProduct, PayWay, Setting, Coupon, Student, TeachCourse, ReceiveCoupon, StudyRecord, \
    TeacherEvaluate, StudentEvaluate, AgainStudyApply, Order, OrderDetail, ShoppingCar, Complain, ReviseCourse, \
    StudentCollectTeacher, StudentShareTeacher, MainCategory, SubCategory, SmallCategory, CourseCategory, Unit


class FrontPageSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'action', )
    list_display_links = ('title', 'description', 'action', )

admin.site.register(FrontPageSlider, FrontPageSliderAdmin)

 # register table,then you can find talbe in the suit(admin platment)
class ComboTypeAdmin(admin.ModelAdmin):
    list_display = ('combo_name', 'user', )
    list_display_links = ('combo_name', 'user', )

admin.site.register(ComboType, ComboTypeAdmin)

# class YongEnglishComboAdmin(admin.ModelAdmin):
#     list_display = ('yong_name',)
#
# admin.site.register(YongEnglishCombo, YongEnglishComboAdmin)

class CountComboAdmin(admin.ModelAdmin):
    list_display = ('count_name', 'count_number', 'valid_date', 'money', )
    list_display_links = ('count_name', 'count_number', 'valid_date', 'money', )
    search_fields = ('count_name', 'count_number', 'valid_date', 'money', )

admin.site.register(CountCombo, CountComboAdmin)

class MonthComboAdmin(admin.ModelAdmin):
    list_display = ('month_name', 'month_number', 'valid_date', 'money', )
    list_display_links = ('month_name', 'month_number', 'valid_date', 'money', )
    search_fields = ('month_name', 'month_number', 'valid_date', 'money', )

admin.site.register(MonthCombo, MonthComboAdmin)

# # class MiddleTeachComboAdmin(admin.ModelAdmin):
# #     list_display = ('name',)
# #
# # admin.site.register(MiddleTeachCombo, MiddleTeachComboAdmin)
#
# class DocTypeAdmin(admin.ModelAdmin):
#     list_display = ('type_name',)
#     list_display_links = ('type_name',)
#
# admin.site.register(DocType, DocTypeAdmin)

# class CourseTypeAdmin(admin.ModelAdmin):
#     list_display = ('type_name', )
#     list_display_links = ('type_name', )
#
# admin.site.register(CourseType, CourseTypeAdmin)

#use super-inline
# class SmallCategoryInlineAdmin(SuperInlineModelAdmin, TabularInline):
#     model = SmallCategory
#     extra = 1
#
# class SubCategoryInlineAdmin(SuperInlineModelAdmin, StackedInline):
#     model = SubCategory
#     extra = 1
#     inlines = [SmallCategoryInlineAdmin,]
#
# class MainCategoryAdmin(SuperModelAdmin):
#
#     list_display = ('id', 'main_name',)
#     list_display_links = ('id', 'main_name',)
#     inlines = [SubCategoryInlineAdmin,]
#
# admin.site.register(MainCategory, MainCategoryAdmin)

# use nest-inline
class MainCategoryAdmin(NestedModelAdmin):
    list_display = ('id', 'main_name',)
    list_display_links = ('id', 'main_name',)

    inlines = [SubCategoryInline]

admin.site.register(MainCategory, MainCategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_main_name', 'sub_name',) # 定义admin总览里每行的显示信息，由于main_name是在subcategory的外键maincategory表中，所以需要特殊返回，注意这个字段不能用main_category__main_name的形式
    list_display_links = ('id', 'sub_name',)
    list_filter = ('main_category__main_name', ) # 定义列表过滤,如果有外键则使用main_category__main_name形式

    inlines = [SmallCategoryInline]


    def get_main_name(self, obj): # 定义这个函数是由于main_name是在subcategory表中的外键表maincategory里，所以需要单独return-下
        return obj.main_category.main_name
    get_main_name.short_description = u'主分类名' # list展示时候显示的title


admin.site.register(SubCategory, SubCategoryAdmin)

class SmallCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_sub_main_name', 'get_sub_sub_name',  'small_name', )
    list_display_links = ('id', 'small_name', )
    list_filter = ('main_sub_category__main_category__main_name', 'main_sub_category__sub_name', )

    def get_sub_main_name(self,obj):
        return obj.main_sub_category.main_category.main_name
    get_sub_main_name.short_description = u'主分类名'

    def get_sub_sub_name(self, obj):
        return obj.main_sub_category.sub_name
    get_sub_sub_name.short_description = u'次分类名'

admin.site.register(SmallCategory, SmallCategoryAdmin)

# class DetailCategoryAdmin(admin.ModelAdmin):
#     list_display = ('id',)
#     list_display_links = ('id',)
#     search_fields = ('main_name__main_name', 'sub_name__sub_name', 'small_name__sub_name', )
#
# admin.site.register(DetailCategory, DetailCategoryAdmin)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_name',)
    list_display_links = ('id', 'unit_name',)

admin.site.register(Unit, UnitAdmin)



# class SmallCategoryInline(admin.StackedInline):
#     model = SmallCategory

class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'small_category', 'course',)
    list_display_links =  ('id', 'small_category', 'course',)
    search_fields = ('course__course_name', )

admin.site.register(CourseCategory, CourseCategoryAdmin)

class CourseForm(forms.ModelForm):
    description = forms.CharField(label=u'课程描述', widget=UEditorWidget(width=800, height=500, toolbars={}))


class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    list_display = ('id', 'course_name', 'target',)
    list_display_links = ('id', 'course_name', 'target', )
    search_fields = ('course_name', )
    fieldsets = [
        (None, {'classes': ('wide',), 'fields': ('course_name', 'image', 'target', 'course_number', 'course_unit', 'pay_number',
                                                 'pay_unit', 'student_lv_low', 'student_lv_height',)}),
        (u'课程描述', {'classes': ('full-width',), 'fields': ('description',)})
    ]

admin.site.register(Course, CourseAdmin)


class DocSiteAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'course','doc_name',)
    list_display_links = ('type_name', 'course','doc_name',)
    search_fields = ('course__course_name', )
    list_filter = ('type_name',)

admin.site.register(DocSite, DocSiteAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'course', 'money')
    list_display_links = ('book_name', 'course', 'money')
    search_fields = ('book_name', 'course__course_name', 'money' )

admin.site.register(Book, BookAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'be_good_at_course', 'student_lv', 'teacher_experience', )
    list_display_links = ('teacher_name', 'be_good_at_course', 'student_lv', 'teacher_experience', )
    search_fields = ('teacher_name', 'be_good_at_course', 'student_lv', 'teacher_experience', )

admin.site.register(Teacher, TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'english_name', 'lv', 'mobile','card_number', )
    list_display_links = ( 'english_name', 'lv', 'mobile','card_number', )
    list_filter = ('sex',)
    search_fields = ( 'english_name', 'lv', 'mobile','card_number', )

admin.site.register(Student, StudentAdmin)

class StudentCollectTeacherAdmin(admin.ModelAdmin):
    list_display = ('id', )

admin.site.register(StudentCollectTeacher, StudentCollectTeacherAdmin)

class StudentShareTeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'share_platform', )

admin.site.register(StudentShareTeacher, StudentShareTeacherAdmin)

class FavourableAdmin(admin.ModelAdmin):
    list_display = ('favourable_id', 'favourable_money', 'favourable_description', )
    list_display_links = ('favourable_id', 'favourable_money', 'favourable_description', )
    search_fields = ('favourable_id', 'favourable_money',)

admin.site.register(Favourable, FavourableAdmin)

class FavourableProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', )
    list_display_links = ('product_name', 'product_price', )
    search_fields = ('product_name', 'product_price', )

admin.site.register(FavourableProduct,FavourableProductAdmin)

class PayWayAdmin(admin.ModelAdmin):
    list_display = ('pay_way_type', 'pay_platform', )
    list_display_links = ('pay_way_type', 'pay_platform', )

admin.site.register(PayWay, PayWayAdmin)

class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_id', 'coupon_money', 'valid_date', 'state', )
    list_display_links = ('coupon_id', 'coupon_money', 'valid_date', 'state', )
    list_filter = ('state', )
    search_fields =  ('coupon_id', 'coupon_money', 'valid_date', )

admin.site.register(Coupon, CouponAdmin)

class SettingAdmin(admin.ModelAdmin):
    list_display = ('student', 'short_message', 'auto_substitute',)
    list_display_links =  ('student', 'short_message', 'auto_substitute',)
    search_fields = ('student__id', )
    list_filter = ('short_message', 'auto_substitute', )

admin.site.register(Setting, SettingAdmin)



class TeachCourseAdmin(admin.ModelAdmin):
    list_display = ('course_time', 'course', 'teacher', )
    list_display_links = ('course_time', 'course', 'teacher', )
    search_fields = ('course_time', 'course__course_name', 'teacher__teacher_name', )

admin.site.register(TeachCourse, TeachCourseAdmin)

class ReceiveCouponAdmin(admin.ModelAdmin):
    list_display = ('student', 'coupon', 'receive_time', )
    list_display_links =  ('student', 'coupon', 'receive_time', )
    search_fields = ('student__id', 'coupon__coupon_id', 'receive_time', )

admin.site.register(ReceiveCoupon, ReceiveCouponAdmin)

class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'state', )  # 在页面上显示的字段，若不设置则显示 models.py 中 __unicode__(self) 中所返回的值
    list_display_links = ('student', 'course', 'state', )  # 设置页面上哪个字段可单击进入详细页面
    search_fields = ('student__id', 'course__course_name', )  # 设置搜索栏范围，如果有外键，要注明外键的哪个字段，双下划线
    list_filter = ('state', )

admin.site.register(StudyRecord, StudyRecordAdmin)

class ComplainAdmin(admin.ModelAdmin):
    list_display = ('complain_reason', 'complain_content', )
    list_display_links = ('complain_reason', 'complain_content', )
    list_filter = ('complain_reason', )

admin.site.register(Complain, ComplainAdmin)

class ReviseCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_doc', )
    list_display_links = ('id', 'class_doc', )

admin.site.register(ReviseCourse, ReviseCourseAdmin)

class TeacherEvaluateAdmin(admin.ModelAdmin):
    list_display = ('study_record', 'current_lv', 'pronunication', 'performance',)
    list_display_links = ('study_record', 'current_lv', 'pronunication', 'performance',)
    search_fields = ('study_record__id',)
    list_filter = ('pronunication', 'grammar', 'vocabulary', 'fluency', 'listening', )

admin.site.register(TeacherEvaluate, TeacherEvaluateAdmin)

class StudentEvaluateAdmin(admin.ModelAdmin):
    list_display = ('study_record','time',  )
    list_display_links = ('study_record',  'time', )
    search_fields = ('study_record__id', 'time', )

admin.site.register(StudentEvaluate, StudentEvaluateAdmin)

class AgainStudyApplyAdmin(admin.ModelAdmin):
    list_display = ('study_record', 'reason', )
    list_display_links = ('study_record', 'reason', )

admin.site.register(AgainStudyApply, AgainStudyApplyAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'favourable_money', 'capital', 'state', )
    list_display_links = ('order_id', 'favourable_money', 'capital', 'state', )
    list_filter = ('state', )
    search_fields = ('order_id',)

admin.site.register(Order, OrderAdmin)

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'pay_way', 'quantity', )
    list_display_links = ('order', 'pay_way', 'quantity', )
    search_fields = ('quantity', )

admin.site.register(OrderDetail, OrderDetailAdmin)

class ShoppingCarAdmin(admin.ModelAdmin):
    list_display = ('student', )
    search_fields = ('student__id',)

admin.site.register(ShoppingCar, ShoppingCarAdmin)




