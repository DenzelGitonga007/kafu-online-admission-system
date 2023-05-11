from django.contrib import admin

# Register your models here.
from .models import Student, PersonalDetail

admin.site.register(Student)
admin.site.register(PersonalDetail)
