from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from student.models import StudentList
from teacher.models import Course,AttendanceDB
from subadmin.models import Class
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
def landingPage(request):
    return render(request,'landing.html')


    
@login_required
def index(request):
    usr_dl=StudentList.objects.filter(user=request.user).values()
    course = Course.objects.filter(student_code = usr_dl[0]['id']).values()
    
    
    lst = []
    for i in course:
        std = i['subject_code']
        
        clas = Class.objects.filter(course_code = std).values()
        print(clas)
        lst.append(clas[0])


    student_list = StudentList.objects.filter()
    diction = {
        'text':'i am a text from akash',
        'name':'akash',
        'course':lst,
    
    }
    return render(request,'student/dashboard.html',context = diction)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username = username,password = password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                dict = {
                    'user':user
                }
                return HttpResponseRedirect(reverse('student:index'))
                #return render(request,'student/dashboard.html',context = dict)

            else:
                return HttpResponse('Account is not active')
        else:
            return HttpResponse('Login unsuccesfull')
    else:
        return render(request,'student/auth/login.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('student:login'))

def register(request):
    diction = {}
    if request.method == 'POST':
        student=StudentList()
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        
        user.set_password(request.POST.get('password'))
        users = user.save()
        
        student.user = user
        student.student_id= request.POST.get('student_id')
        student.first_name= request.POST.get('first_name')
        student.last_name= request.POST.get('last_name')
        student.year= request.POST.get('year')
        student.semister = request.POST.get('semister')
        student.section = request.POST.get('section')
        
        student.save()
        return render(request,'student/auth/login.html',context = diction)
    else:
        
        return render(request,'student/auth/register.html',context = diction)


def addView(request):
    usr_dl=StudentList.objects.filter(user=request.user).values()
    course = Course.objects.filter(student_code = usr_dl[0]['id']).values()
    print(usr_dl[0]['student_id'])
    print(course)

    dict = {
        'usr_dl':usr_dl[0],
        'course':course,
        'student_id':usr_dl[0]['student_id'],
    }
    return render(request,'student/view/create.html',context = dict)

def showAttendance(request):
    if request.method == 'POST':
        std = request.POST.get('student_id')
        course_code = request.POST.get('course_code')
        res = AttendanceDB.objects.filter(course_code = course_code,student_id=std).values()
        dict = {
            'details':res
        }
        return render(request,'student/view/show.html',context = dict)


    

