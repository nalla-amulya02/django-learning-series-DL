from django.contrib import admin

from accounts.models import Student

# Register your models here.
admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','email')
