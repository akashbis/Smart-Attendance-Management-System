from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from subadmin.models import SubAdmin , Class
from teacher.models import Teacher
from django.contrib.auth.models import User
from subadmin.forms import SubAdminForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def index(request):
    usr_dl=SubAdmin.objects.filter(user=request.user).values()
    a = usr_dl[0]['user_id']
    usr = User.objects.filter(id = a).values()
    teacher = obj = Teacher.objects.all()
    dict = {
        'usr_dl':usr_dl[0],
        'usr':usr[0],
        'teacher':teacher
    }
    return render(request,'admin/dashboard.html',context = dict)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                
                dict = {
                    'user':user,
                    
                }
                return HttpResponseRedirect(reverse('subadmin:index'))
                #return render(request,'student/dashboard.html',context = dict)

            else:
                return HttpResponse('Account is not active')
        else:
            return HttpResponse('Login unsuccesfull')
    else:
        return render(request,'admin/auth/login.html')

@login_required
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('subadmin:login'))

@login_required
def showClass(request):
    usr_dl=SubAdmin.objects.filter(user=request.user).values()
    user = Class.objects.all()
    dict = {
        'user':request.user,
        'usr_dl':usr_dl[0],
        'class':user,
        
    }
    
    return render(request,'admin/showclass.html',context = dict)
    
@login_required
def createClass(request):
    if request.method == 'POST':

        obj = Class()
        obj.course_code = request.POST.get('course_code')
        obj.course_name = request.POST.get('course_name')
        obj.course_teacher = request.POST.get('course_teacher')
        obj.department = request.POST.get('department')
        obj.year = request.POST.get('year')
        obj.semister = request.POST.get('semister')
        obj.save()
        return HttpResponseRedirect(reverse('subadmin:showclass'))

    else:
        usr_dl=SubAdmin.objects.filter(user=request.user).values()
        teacher = Teacher.objects.all()
        dict = {
            'user':request.user,
            'usr_dl':usr_dl[0],
            'teacher':teacher,
            
        }
        return render(request,'admin/class.html',context = dict)
@login_required
def updateClass(request):

    obj = Class.objects.get(id = request.POST.get('id'))
    print(request.POST.get('course_code'))
    obj.course_code = request.POST.get('course_code')
    obj.course_name = request.POST.get('course_name')
    obj.course_teacher = request.POST.get('course_teacher')
    obj.department = request.POST.get('department')
    obj.year = request.POST.get('year')
    obj.semister = request.POST.get('semister')
    obj.save()
    return HttpResponseRedirect(reverse('subadmin:showclass'))
        
    
    
@login_required
def deleteClass(request,id):
    clas = Class.objects.get(id = id)
    clas.delete()
    return HttpResponseRedirect(reverse('subadmin:showclass'))

@login_required
def editClass(request,id):
    clas = Class.objects.get(id = id)
    teacher = Teacher.objects.all()
    usr_dl=SubAdmin.objects.filter(user=request.user).values()
    dict = {
        'class':clas,
        'teacher':teacher,
        'usr_dl':usr_dl[0],

    }
    return render(request,'admin/editclass.html',context=dict)