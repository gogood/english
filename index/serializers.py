# coding: utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import serializers
from index.models import MainCategory, SubCategory, SmallCategory, Course, TeachCourse


#
class SmallCategorySerializer(serializers.ModelSerializer):
     title = serializers.CharField(source='small_category_name')

     class Meta:
         model = SmallCategory
         fields = ( 'id', 'title',)

class SubCategorySerializer(serializers.ModelSerializer):
    children = SmallCategorySerializer(source='smallcategory_set', instance=id, many=True, read_only=True) # many=True one to many
    title = serializers.CharField(source='sub_category_name')

    class Meta:
        model = SubCategory
        fields = ('id', 'title', 'children', )

class MainCategorySerializer(serializers.ModelSerializer):
    children = SubCategorySerializer(source='subcategory_set', many=True, read_only=True)
    title = serializers.CharField(source='main_category_title')

    class Meta:
        model = MainCategory
        fields = ('id', 'title','children', )

class TeachCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeachCourse
        fields = ('course_time', 'teacher', )


class CourseSerializer(serializers.ModelSerializer):
    other = TeachCourseSerializer(source='teachcourse_set', many=True)
    # unit_course = serializers.CharField(source='course_unit.unit_name') #取外键（-对多 在一中取）
    number_course = serializers.SerializerMethodField()
    pay = serializers.SerializerMethodField()
    student_lv = serializers.SerializerMethodField()

    def get_number_course(self, obj):
        return '%s%s' % (obj.course_number, obj.course_unit)

    def get_pay(self, obj):
        return '%s%s' % (obj.pay_number, obj.pay_unit)

    def get_student_lv(self, obj):
        if (obj.student_lv_low == obj.student_lv_height):
            return '%s' % (obj.get_student_lv_low_display())
        else:
            return '%s~%s' % (obj.get_student_lv_low_display(), obj.get_student_lv_height_display())

    class Meta:
        model = Course
        fields = (
        'id', 'number_course', 'course_name', 'description', 'image', 'target', 'number_course', 'pay', 'student_lv',
        'other',)


class PaginatedCourseSerializer():
    def __init__(self, courses, num, page):
        paginator = Paginator(courses, num) # show num courses per page
        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
             # If page is not an integer, deliver first page.
            courses = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            courses = paginator.page(paginator.num_pages)
        count = paginator.count # num_total

        # previous = None if not courses.has_previous() else courses.previous_page_number()
        # next = None if not courses.has_next() else courses.next_page_number()
        serializer = CourseSerializer(courses, many=True)

        self.data = {'current_page':page, 'num_per_page':num, 'total_page_count': paginator.num_pages, 'total_course_count': count, 'total_current_course': len(serializer.data), 'courses':serializer.data}

        # self.data = {'current_page':page, 'num_per_page':num, 'total_page_count': paginator.num_pages, 'total_course_count': count, 'previous': previous, 'next': next, 'courses':serializer.data}



#

#

# class DetailCategorySerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(source='sub_category_id', read_only=True,)
#     title = serializers.CharField(source='sub_category_title', read_only=True,)
#     children = SmallCategorySerializer()
#     class Meta:
#         model = DetailCategory
#         fields = ('id', 'title', 'children')






