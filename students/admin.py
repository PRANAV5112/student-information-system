

from django.contrib import admin
from .models import Student, Parent, Grade

# Register your models here.
# This makes the Student and Parent models visible on the admin site.
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Grade)  