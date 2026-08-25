from django.contrib import admin
from .models import Student
# Register your models here.

# class StudentAdmin(admin.ModelAdmin):
#     list_display=['name','age','email','city']

# admin.site.register(Student,StudentAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','email','city']
    search_fields=['city','age']
    list_filter = ['city','age'] 
