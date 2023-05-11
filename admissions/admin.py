from django.contrib import admin

# Register your models here.
from .models import Student, PersonalDetail

# To customize the Student display
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_username',)

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    
# class PersonalDetailAdmin(admin.ModelAdmin):
#     list_display = ('student', 'surname', 'first_name', 'last_name', 'email', 'phone', 'city', 'get_username')
#     list_select_related = ('student',)

#     def get_username(self, obj):
#         return obj.student.user.username
#     get_username.short_description = 'Username'
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('id','surname', 'first_name', 'last_name', 'email', 'phone', 'city')





admin.site.register(Student, StudentAdmin)
admin.site.register(PersonalDetail, PersonalDetailAdmin)
