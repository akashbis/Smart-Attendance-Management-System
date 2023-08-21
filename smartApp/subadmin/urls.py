from django.contrib import admin
from django.urls import path
from subadmin import views
app_name = 'subadmin'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('login/',views.admin_login, name = 'login'),
    path('logout/',views.admin_logout, name = 'logout'),
    path('addclass/',views.createClass,name = 'addclass'),
    path('showclass/',views.showClass,name = 'showclass'),
    path('editclass/<int:id>',views.editClass),
    path('updateclass/',views.updateClass, name = 'updateclass'),
    path('deleteclass/<int:id>',views.deleteClass),

    
]