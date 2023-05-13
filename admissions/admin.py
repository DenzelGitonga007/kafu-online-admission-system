from django.contrib import admin

# Register your models here.
from .models import PersonalDetail, ParentDetail, SpouseDetail, NextKinDetail, HighSchoolDetail

# To customize the Student display
# Get the username for all details
def username(obj):
    return obj.user.username

# Personal details
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = (username,'surname', 'first_name', 'last_name', 'email', 'phone', 'city')

# Parent details
class ParentDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'father_first_name', 'mother_first_name', 'guardian_first_name')

# Spouse details
class SpouseDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'marital_status', 'spouse_first_name')

# Next of Kin details
class NxtkDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'nxtk_first_name')

# High School details
class HighSchoolDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'first_high_school_name')

admin.site.register(PersonalDetail, PersonalDetailAdmin) # Personal details
admin.site.register(ParentDetail, ParentDetailAdmin) # Parent details
admin.site.register(SpouseDetail, SpouseDetailAdmin) # Spouse details
admin.site.register(NextKinDetail, NxtkDetailAdmin) # Spouse details
admin.site.register(HighSchoolDetail, HighSchoolDetailAdmin) # High School details
