from django.db import models

# Create your models here.
class Student(models.Model): 
    name = models.CharField(max_length=100) 
    age = models.IntegerField(default=None) 
    marks = models.IntegerField(default=None) 
    city = models.CharField(max_length=50) 
    course = models.CharField(max_length=50,default=None) 
    fees = models.IntegerField(default=None) 
 
    def __str__(self): 
        return self.name
       