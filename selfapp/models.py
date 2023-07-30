from django.db import models

# Create your models here.
...
# class Student(models.Model):
#     name = models.CharField(max_length=40)
#     rollnumber = models.CharField(max_length=20)
#     address = models.TextField()
    
class person(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    is_student = models.BooleanField()
    email = models.EmailField()
    message = models.TextField()

class registered_user(models.Model):
    fullname = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
   
    