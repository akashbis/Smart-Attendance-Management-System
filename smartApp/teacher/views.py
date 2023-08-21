from django.shortcuts import render
from teacher.models import Teacher, Course ,AttendanceDB
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User
from subadmin.models import Class
from student.models import StudentList
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
import cv2

@login_required
def index(request):
    usr_dl=Teacher.objects.filter(user=request.user).values()
    teacher_id = usr_dl[0]['id']
    course_details = Class.objects.filter(course_teacher = teacher_id).values()
    

    dict = {
        'usr_dl':usr_dl[0],
        'course':course_details,
    }
    return render(request,'teacher/dashboard.html',context = dict)

def user_login(request):
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
                return HttpResponseRedirect(reverse('teacher:index'))
                #return render(request,'student/dashboard.html',context = dict)

            else:
                return HttpResponse('Account is not active')
        else:
            return HttpResponse('Login unsuccesfull')
    else:
        return render(request,'teacher/auth/login.html')

def register(request):
    diction = {
        'success':'Registration Successfully'
    }
    if request.method == 'POST':
        obj=Teacher()
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        
        user.set_password(request.POST.get('password'))
        users = user.save()
        
        obj.user = user
        obj.first_name= request.POST.get('first_name')
        obj.last_name= request.POST.get('last_name')
        obj.mobile_number= request.POST.get('mobile_number')
        obj.dept = request.POST.get('department')
        obj.faculty = request.POST.get('faculty')
        obj.designation = request.POST.get('desigation')
        
        obj.save()
        return render(request,'teacher/auth/login.html',context = diction)
    else:
        
        return render(request,'teacher/auth/register.html',context = diction)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('teacher:login'))

def getStudentByYear(request,subject):
    course = Course.objects.filter(subject_code = subject).values()
    usr_dl=Teacher.objects.filter(user=request.user).values()
    lst = []
    for i in course:
        std = i['student_code']
        student = StudentList.objects.filter(id = std).values()
        lst.append(student[0])
    
    dict = {
        'usr_dl':usr_dl[0],
        'student':lst,
        
    }
    return render(request,'teacher/addstudent.html',context=dict)


def showStudentByTeacher(request):
    usr_dl=Teacher.objects.filter(user=request.user).values()
    if request.method == 'POST':
        year = request.POST.get('year')
        semister = request.POST.get('semister')
        dept = request.POST.get('department')
        subject = request.POST.get('subject')
        obj = StudentList.objects.filter(year = year,semister = semister,department = dept).values()
        

        dict = {
            'usr_dl':usr_dl[0],
            'student':obj,
            'subject':subject,
            'year':year,
            'semister':semister,
            'dept':dept,
        }

        
        return render(request,'teacher/student/showStudent.html',context=dict)

    else:
        teacher = Teacher.objects.filter(user=request.user).values()
        teacher_id = teacher[0]['id']
        subject = Class.objects.filter(course_teacher = teacher_id).values()
        
        dict = {
            'usr_dl':usr_dl[0],
            'teacher_id' : teacher[0]['id'],
            'subject':subject,
        }
        return render(request,'teacher/student/studentAddCourse.html',context=dict)


def insertStdWiCourse(request):
    std_code = request.POST.getlist('std_id')
    subject_code = request.POST.get('subject')
    for i in std_code:
        obj = Course()
        obj.student_code = i
        obj.subject_code = subject_code
        obj.save()
    
    return HttpResponseRedirect(reverse('teacher:showStudentByTeacher'))

def takeAttendance(request):
    usr_dl=Teacher.objects.filter(user=request.user).values()
    teacher = Teacher.objects.filter(user=request.user).values()
    teacher_id = teacher[0]['id']
    subject = Class.objects.filter(course_teacher = teacher_id).values()
    print(teacher_id)
    dict = {
        'usr_dl':usr_dl[0],
        'teacher_id' : teacher[0]['id'],
        'subject':subject,
    }
    return render(request,'teacher/attendance/takeAtten.html',context=dict)

def addAttendance(request):
    if request.method == 'POST':
        subject_code = request.POST.get('subject')
        subject_name = Class.objects.filter(course_code = subject_code).values()
        usr_dl=Teacher.objects.filter(user=request.user).values()
        course = Course.objects.filter(subject_code = subject_code).values()
        
        lst = []
        for i in course:
            std = i['student_code']
            student = StudentList.objects.filter(id = std).values()
            lst.append(student[0])

        
        dict = {
            'usr_dl':usr_dl[0],
            'course_name':subject_name[0]['course_name'],
            'course_code':subject_code,
            'student':lst
            
        }
        return render(request,'teacher/attendance/addAtten.html',context=dict)
    else:
        pass


    


def Attendance(request):
    
    if request.method == 'POST':
        course_code = request.POST.get('course_code')
        student_id = request.POST.getlist('student_id')
        course_name = request.POST.get('course_name')
        comment = request.POST.getlist('comment')
        first_name = request.POST.getlist('first_name')
        last_name = request.POST.getlist('last_name')

        if 'auto' in request.POST:
            cap = cv2.VideoCapture(0)
            while(True):
                ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                cv2.imshow('frame',frame)
                if cv2.waitKey(20) & 0xFF == ord('q'):
                    break
        
        

            cap.release()
            cv2.destroyAllWindows()
            return render(request,'teacher/attendance/addAtten.html')

        else:
            
        
            print(course_code)
        
            rang  = range(len(student_id))
            for i in rang:
                x = datetime.datetime.now()
                d = datetime.date(x.year,x.month,x.day)

            
                atn = AttendanceDB()
                atn.course_code = course_code
                atn.student_id = student_id[i]
                atn.comment = comment[i]
                atn.status = request.POST.get(student_id[i])
                atn.at_date = d
                atn.save()
            return render(request,'teacher/attendance/addAtten.html')


        

    else:
        pass

def showAttendance(request):
    usr_dl=Teacher.objects.filter(user=request.user).values()
    teacher_id = usr_dl[0]['id']
    
    details = Class.objects.filter(course_teacher = teacher_id).values()
    print(details)
    dict={
        'usr_dl':usr_dl[0],
        'course':details,
        'teacher_id':teacher_id,
    }
    return render(request,'teacher/attendance/create.html',context = dict)


def viewAttendance(request):
    usr_dl=Teacher.objects.filter(user=request.user).values()
    if request.method == 'POST':
        course_code = request.POST.get('course_code')
        res = AttendanceDB.objects.filter(course_code = course_code).values()
        print(res)
        dict = {
            'usr_dl':usr_dl[0],
            'details':res
        }
        return render(request,'teacher/attendance/show.html',context = dict)

    


    



