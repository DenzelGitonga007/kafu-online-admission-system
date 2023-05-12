from django.contrib import admin

# Register your models here.
from .models import PersonalDetail, ParentDetail

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

admin.site.register(PersonalDetail, PersonalDetailAdmin) # Personal details
admin.site.register(ParentDetail, ParentDetailAdmin) # Parent details
