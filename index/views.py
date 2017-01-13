# -*- coding: UTF-8 -*-
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from index.models import FrontPageSlider, Course, MainCategory, SubCategory, SmallCategory, CourseCategory, Student
from index.serializers import MainCategorySerializer, SubCategorySerializer, CourseSerializer, PaginatedCourseSerializer
import json
from django.db.models import Count, Q

# session(on same session)
def is_login(request):
    student = ''
    if request.session.has_key('user'):
            print 'get_session'
            id = request.session['user']
            student = Student.objects.get(id=id)
            return student
    return student


@csrf_exempt
def index(request):

    sliders = FrontPageSlider.objects.all()

    if request.method == 'GET':

        if(is_login(request) != ''):
        # if request.session.has_key('user'):
            # print 'get_session'
            # id = request.session['user']
            # student = Student.objects.get(id=id)
            student = is_login(request)
            context = {'sliders': sliders,'is_login': {'result': 'true', 'student': student.english_name}}
            return render(request, 'index.html',context)
        if 'loreUser' in request.COOKIES and 'mobile' in request.COOKIES and 'password' in request.COOKIES:
            print '123'
            is_mobile = Student.objects.filter(mobile=request.COOKIES['mobile'])
            if check_password(request.COOKIES['password'], is_mobile[0].password):
                request.session['user'] = is_mobile[0].id
                student = is_mobile[0].english_name
                context = {'sliders': sliders,'is_login': {'result': 'true', 'student': student}}
                return render(request, 'index.html',context)
    context = {'sliders': sliders}
    return render(request, 'index.html', context)


def course(request):
    if request.method == 'GET':
            if(is_login(request) != ''):
                student = is_login(request)
                context = {'is_login': {'result': 'true', 'student': student.english_name}}
                return render(request, 'course.html',context)
            return render(request, 'course.html')


def course_detail(request):
    return render(request, 'courseDetail.html')


def api_course(request):
    response_data = {}
    # get navigation_data (total_category_data)
    main = MainCategory.objects.all()
    serializer = MainCategorySerializer(main, many=True)  # many=True show list(has many item)
    response_data['category'] = serializer.data
    course_data = Course.objects.all().order_by('teachcourse__course_time')
    serializer1 = PaginatedCourseSerializer(course_data, 20, 1)
    response_data['courses'] = serializer1.data
    response = HttpResponse(json.dumps({'response_data': response_data}), content_type="application/json")
    return response
    # return JsonResponse(response_data, safe=False)


@csrf_exempt
def api_course_category(request):
    if request.method == 'POST':
        # result_char request.body
        json_all = json.loads(request.body)
        print({'api_json_all': json_all})
        current_page = json_all['current_page']
        num_per_page = json_all['num_per_page']
        tag = json_all['tag']
        id_1 = tag['id_1']
        children = tag['children']
        order = json_all['order']
        sort = json_all['sort']
        # id_2 =[]
        id_3 = []
        for i in children:
            # id_2.append(i['id_2'])
            id_3.append(i['id_3'])
        print({'children.len': len(children) <= 0})

        if len(children) > 0:
            if order == 'time':
                print({'time': 'time'})
                if sort == '+':
                    courses = Course.objects.filter(coursecategory__small_category__in=id_3). \
                        order_by('teachcourse__course_time')
                else:
                    courses = Course.objects.filter(coursecategory__small_category__in=id_3). \
                        order_by('-teachcourse__course_time')
            if order == 'price':
                print({'price': 'price'})
                if sort == '+':
                    courses = Course.objects.filter(coursecategory__small_category__in=id_3). \
                        order_by('pay_number')
                else:
                    courses = Course.objects.filter(coursecategory__small_category__in=id_3). \
                        order_by('-pay_number')
            if order == 'population':
                print({'population': 'population'})
                if sort == '+':
                    courses = Course.objects.filter(coursecategory__small_category__in=id_3) \
                        .annotate(num_studyrecords=Count('studyrecord')) \
                        .order_by('num_studyrecords')
                else:
                    courses = Course.objects.filter(coursecategory__small_category__in=id_3) \
                        .annotate(num_studyrecords=Count('studyrecord')) \
                        .order_by('-num_studyrecords')
        else:
            if id_1 == 'all':
                if order == 'time':
                    print({'all_[]_time': 'time'})
                    if sort == '+':
                        courses = Course.objects.order_by('teachcourse__course_time')
                    else:
                        courses = Course.objects.order_by('-teachcourse__course_time')
                if order == 'price':
                    print({'all_[]_price': 'price'})
                    if sort == '+':
                        courses = Course.objects.order_by('pay_number')
                    else:
                        courses = Course.objects.order_by('-pay_number')
                if order == 'population':
                    print({'all_[]_price': 'population'})
                    if sort == '+':
                        courses = Course.objects.annotate(num_studyrecords=Count('studyrecord')). \
                            order_by('num_studyrecords')
                    else:
                        courses = Course.objects.annotate(num_studyrecords=Count('studyrecord')). \
                            order_by('-num_studyrecords')
            else:
                if order == 'time':
                    print({'[]_time': 'time'})
                    if sort == '+':
                        courses = Course.objects.filter(
                            coursecategory__small_category__main_sub_category__main_category=id_1). \
                            order_by('teachcourse__course_time')
                    else:
                        courses = Course.objects.filter(
                            coursecategory__small_category__main_sub_category__main_category=id_1). \
                            order_by('-teachcourse__course_time')
                if order == 'price':
                    print({'[]_price': 'price'})
                    if sort == '+':
                        courses = Course.objects.filter(
                            coursecategory__small_category__main_sub_category__main_category=id_1). \
                            order_by('pay_number')
                    else:
                        courses = Course.objects.filter(
                            coursecategory__small_category__main_sub_category__main_category=id_1). \
                            order_by('-pay_number')
                if order == 'population':
                    print({'[]_population': 'population'})
                    if sort == '_':
                        courses = Course.objects.filter(
                            coursecategory__small_category__main_sub_category__main_category=id_1). \
                            annotate(num_studyrecords=Count('studyrecord')).order_by('num_studyrecords')
                    else:
                        courses = Course.objects.filter(
                            coursecategory__small_category__main_sub_category__main_category=id_1). \
                            annotate(num_studyrecords=Count('studyrecord')).order_by('-num_studyrecords')
    serializer = PaginatedCourseSerializer(courses, num_per_page, current_page)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_course_search(request):
    if request.method == 'POST':
        json_all = json.loads(request.body)
        # print ({json_all: json_all})
        current_page = json_all['current_page']
        num_per_page = json_all['num_per_page']
        keyword = json_all['keyword']
        courses = Course.objects.filter(
            Q(course_name__contains=keyword) | Q(coursecategory__small_category__small_name__contains=keyword) | Q(
                coursecategory__small_category__main_sub_category__sub_name__contains=
                keyword) | Q(coursecategory__small_category__main_sub_category__main_category__main_name__contains
                             =keyword)).distinct()

        serializer = PaginatedCourseSerializer(courses, num_per_page, current_page)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_center(request):
    if request.method == 'GET':
        id = request.session['user']
        student = Student.objects.get(id=id)
        context = {'student': student}
        return render(request, 'userCenter.html',context)
    else:
        return redirect('index')

def user(request):
    return render(request, 'usertest.html')

@csrf_exempt
def api_login(request):
    if request.method == 'POST':
        print 'api_login'
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        print mobile
        print password
        is_mobile = Student.objects.filter(mobile=mobile)
        if len(is_mobile) <= 0:
            result = 'false'
        else:
            # print is_mobile
            # print check_password(password, is_mobile[0].password)
            if check_password(password, is_mobile[0].password):
                request.session['user'] = is_mobile[0].id
                print 1234
                student = is_mobile[0].english_name
                result = 'true'
                return JsonResponse({'result': result, 'student': student})
                # return redirect('index')
                # print 1234
                # result = 'true'
            else:
                print 222234
                result = 'false'
    else:
        if request.session.has_key('user'):  
            id = request.session['user']
            # student = Student.objects.get(id=id)
            # print student
            # name = student.english_name
            result = 'true'
            return JsonResponse({'result': result, 'student': id})
        else:
            result = 'false'
    return JsonResponse({'result': result})

def register(request):
   return render(request, 'register.html')

@csrf_exempt
def register_message_validate(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        validate_code = request.POST.get('validate_message')
        print({'mobile':mobile})
        print({'validate_message':validate_code})
        appkey = "23583402"
        secret = "5ddc3357c11fdf912fa936c29e68bba2"
        req = top.api.AlibabaAliqinFcSmsNumSendRequest()
        req.set_app_info(top.appinfo(appkey, secret))
        code = {"code":validate_code}
        send_code = json.dumps(code)
        req.sms_type="normal"
        req.sms_free_sign_name="neva轻微"
        # req.sms_param='{"code":"1234"}'
        req.sms_param = send_code  # use str(code) will create code:u''
        # req.rec_num="13527114589"
        req.rec_num = str(mobile) # must add str,
        req.sms_template_code="SMS_36320050"

        try:
           resp = req.getResponse()
           return JsonResponse({'resp': resp})
        except Exception,e:
            return JsonResponse({'e': e})
    else:
        return redirect('index')

@csrf_exempt
def api_apply(request):
    if request.method =='POST':
        all_data = json.loads(request.body)
        mobile = all_data['mobile']
        password = all_data['password']
        englisth_name = all_data['englisth_name']
        recom_mobile = all_data['recom_mobile']
        new_password = make_password(password)
        print {'mobile': mobile}
        print {'password': password}
        print {'englisth_name': englisth_name}
        print {'recom_mobile': recom_mobile}
        if len(recom_mobile)>0:
            student = Student(mobile = mobile, password = password, englisth_name = englisth_name, recomment_mobile = recom_mobile, is_apply_course = 0)
        else:
            student = Student(mobile = mobile, password=new_password, english_name=englisth_name, is_apply_course = 0)
        student.save()
        request.session['user'] = student.id
        return JsonResponse({'result': 'true'})
    else:
        return redirect('index')
        # sliders = FrontPageSlider.objects.all()
        # context = {'sliders': sliders}
        # return HttpResponseRedirect('/index/', context)

@csrf_exempt
def api_register(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        birthday = request.POST.get('birthday')
        recom_mobile = request.POST.get('recomment_mobile')
        new_password = make_password(password)
        print({'new':new_password})
        print({'mobile':mobile})
        print({'birthday':birthday})
        # bithda = datetime.datetime(1940, 10, 22)
        # bi = datetime.strptime(birthday, '%b %d %Y')
        # print({'bit':bi})
        if len(recom_mobile)>0:
            student = Student(mobile = mobile, password = new_password, birthday = birthday, recomment_mobile = recom_mobile)
        else:
            student = Student(mobile = mobile, password = new_password, birthday = birthday)
        result = student.save()
        request.session['user'] = student.id
        print result
        return JsonResponse({'result':'true'})
        # student.save(force_insert=True)
        # print({'student': student})
        # print ({'save': student.save()})
        # result = Student.objects.create(mobile = mobile, password = new_password, birthday = birthday)
        # print({'result':result})
        return JsonResponse({'result': 'false'})
    else:
        return redirect('index')

def forget_password(request):
    return render(request, 'forget_password.html')

# exit
# delete brower cookie
def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
        sliders = FrontPageSlider.objects.all()
        context = {'sliders': sliders}
        response = render(request, 'index.html',context)
        response.delete_cookie('loreUser')
        response.delete_cookie('mobile')
        response.delete_cookie('password')
        return response
    else:
        return redirect('index')


    # sliders = FrontPageSlider.objects.all()
    # context = {'sliders': sliders}
    # # response = render(request, 'index.html',context)
    # print '1234'
    # request.delete_cookie('loreUser')
    # print {'lore': request.COOKIES.get('loreUser')}
    # request.delete_cookie('mobile')
    # request.delete_cookie('password')
    # print {'user': request.session['user']}



    # try:
    #    sliders = FrontPageSlider.objects.all()
    #    response = redirect('index')
    #    lore = response.delete_cookie('loreUser')
    #    print {'lore': response.COOKIES.get('loreUser')}
    #    response.delete_cookie('mobile')
    #    response.delete_cookie('password')
    #    print {'user': request.session['user']}
    #    del request.session['user']
    # return response
    # except:
    #     print 'except'
    #     pass
    # response.delete_cookie('sessionid')

    # response.set_cookie('loreUser', '')

def apply(request):
    if request.method == 'GET':
        if request.session.has_key('user'):
            return render(request, 'apply.html')
        else:
            sliders = FrontPageSlider.objects.all()
            context = {'sliders': sliders}
            return HttpResponseRedirect('/index/',context)


@csrf_exempt
def api_mobile_is_exist(request):
    if request.method == 'POST':
       mobile = request.POST.get('mobile')
       print mobile
       stu_mo = Student.objects.filter(mobile=mobile)
       if len(stu_mo) > 0:
           result = 'true'
       else:
           result = 'false'
       # print stu_mo
       # if stu_mo != '':
       #     result = 'true'
       # else:
       #     result = 'false'
       return JsonResponse({'result': result})
    else:
        return redirect('index')

@csrf_exempt
def api_forget_password(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        print password
        print mobile
        student = Student.objects.get(mobile=mobile)
        print student
        # create password(hash)
        new_password = make_password(password)
        student.password = new_password
        stu = student.save()
        return JsonResponse({'result': 'true'})
    else:
        return redirect('index')

# def image_up(request):
#     if request.method == 'POST':
#         b = save_file(request.FILES(['upfile']))
#     return HttpResponse(b)
#
# def save_file(file, path=''):
#     print '123456'
#     filename = str(time.time()) + str(random.random()) + file._get_name()
#     print filename
#     fd = open('%s/%s' % (settings.MEDIA_ROOT, str(path)+str(filename)), 'wb')
#     for chunk in file.chunks():
#         fd.write(chunk)
#     fd.close()
#     a = "{'url':'/media/" + filename + "','title':'"+filename+"','state:'SUCCESS'}"
#
#     return a

def test(request):
    return render(request,'usertest.html')