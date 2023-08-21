from django.db import models

from django.contrib.auth.models import User


class StudentList(models.Model):
    #id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length= 50)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    department = models.CharField(max_length=50,default='')
    year = models.CharField(max_length= 50)
    semister = models.CharField(max_length= 50,default = '')
    section = models.CharField(max_length= 50,default = '')
    user_role = models.CharField(max_length=50,default='1')
   

    def __str__(self):
        return self.first_name

        

