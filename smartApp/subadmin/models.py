from django.db import models
from django.contrib.auth.models import User
from teacher.models import Teacher

class SubAdmin(models.Model):
    #id = models.AutoField(primary_key = True)
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    user_role = models.CharField(max_length=50,default='3')
   
    
    def __str__(self):
        return self.first_name


class Class(models.Model):
    course_code = models.CharField(max_length= 50)
    course_name = models.CharField(max_length= 50)
    course_teacher = models.CharField(max_length= 50)
    department = models.CharField(max_length= 50)
    year = models.CharField(max_length= 50)
    semister = models.CharField(max_length= 50)

    def __str__(self):
        return self.course_teacher


