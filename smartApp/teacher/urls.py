from django.contrib import admin
from django.urls import path
from teacher import views
app_name = 'teacher'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('register/',views.register, name = 'register'),
    path('login/',views.user_login, name = 'login'),
    path('logout/',views.user_logout, name = 'logout'),
    path('getstudentbyyear/<str:subject>',views.getStudentByYear,name = 'getstudentbyyear'),
    path('showStudentByTeacher',views.showStudentByTeacher ,name = 'showStudentByTeacher'),
    path('insertstdwicourse',views.insertStdWiCourse ,name = 'insertstdwicourse'),
    path('takeattendance/',views.takeAttendance,name = 'takeattendance'),
    path('addattendance/',views.addAttendance, name = 'addattendance'),
    path('attendance/',views.Attendance, name = 'attendance'),
    path('showattendance/',views.showAttendance,name = 'showattendance'),
    path('viewattendance/',views.viewAttendance,name = 'viewattendance')
    

    
]
