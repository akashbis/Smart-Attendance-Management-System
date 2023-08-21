from django.db import models

import uuid
from django.contrib.auth.models import User


class Teacher(models.Model):
    #id = models.AutoField(primary_key = True)
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    phone_number = models.CharField(max_length= 50)
    dept = models.CharField(max_length= 50)
    faculty = models.CharField(max_length= 50)
    designation = models.CharField(max_length= 50,default = '')
    user_role = models.CharField(max_length=50,default='2')
   
    
    def __str__(self):
        
        return self.first_name

class Course(models.Model):
    student_code = models.CharField(max_length= 50)
    subject_code = models.CharField(max_length= 50)

    def __str__(self):
        return self.student_code +" "+self.subject_code


class AttendanceDB(models.Model):
    course_code = models.CharField(max_length= 50)
    student_id = models.CharField(max_length= 50)
    comment = models.CharField(max_length= 50)
    status = models.CharField(max_length= 50)
    at_date = models.DateField()

    def __str__(self):
        return self.course_code +" "+self.student_id

        

