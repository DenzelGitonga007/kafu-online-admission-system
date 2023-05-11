from django.contrib import admin

# Register your models here.
from .models import Student, PersonalDetail

# To customize the Student display
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_username',)

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'


admin.site.register(Student, StudentAdmin)
admin.site.register(PersonalDetail)
