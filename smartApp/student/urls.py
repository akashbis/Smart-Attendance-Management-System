from django.contrib import admin
from django.urls import path
from student import views
app_name = 'student'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('register/',views.register, name = 'register'),
    path('login/',views.user_login, name = 'login'),
    path('logout/',views.user_logout, name = 'logout'),
    path('addview/',views.addView, name = 'addview'),
    path('showattendance/',views.showAttendance, name = 'showattendance'),
    

    
]
