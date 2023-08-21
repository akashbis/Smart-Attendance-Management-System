
from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from student import views
urlpatterns = [
    path('',views.landingPage,name = "landingPage"),
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),
    path('subadmin/',include('subadmin.urls')),
]
