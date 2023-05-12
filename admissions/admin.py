from django.contrib import admin

# Register your models here.
from .models import PersonalDetail

# To customize the Student display
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('username','surname', 'first_name', 'last_name', 'email', 'phone', 'city')

    def username(self, obj):
        return obj.user.username

# admin.site.register(Student, StudentAdmin)
admin.site.register(PersonalDetail, PersonalDetailAdmin)
