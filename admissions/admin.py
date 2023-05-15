from django.contrib import admin

# Register your models here.
from .models import PersonalDetail, ParentDetail, SpouseDetail, NextKinDetail, HighSchoolDetail, EmergencyContactDetail, GamesDetail, ClubsDetail, OtherInstitutionDetail, OtherDetail, FileDetail

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

# Emergency Contact details
class EmergencyContactDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'emerge_con_first_name')

# Games details
class GamesDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'games_and_sports')

# Clubs
class ClubsDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'first_club')

# Other institution
class OtherInstitutionDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'first_institution_name')

# Other detail
class OtherDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'other_information')

# File detail
class FileDetailAdmin(admin.ModelAdmin):
    list_display = (username, 'photo')

# Register
admin.site.register(PersonalDetail, PersonalDetailAdmin) # Personal details
admin.site.register(ParentDetail, ParentDetailAdmin) # Parent details
admin.site.register(SpouseDetail, SpouseDetailAdmin) # Spouse details
admin.site.register(NextKinDetail, NxtkDetailAdmin) # Spouse details
admin.site.register(HighSchoolDetail, HighSchoolDetailAdmin) # High School details
admin.site.register(EmergencyContactDetail, EmergencyContactDetailAdmin) # Emergency Contact details
admin.site.register(GamesDetail, GamesDetailAdmin)# Games details
admin.site.register(ClubsDetail, ClubsDetailAdmin)# Clubs details
admin.site.register(OtherDetail, OtherDetailAdmin)# Other Institution details
admin.site.register(OtherInstitutionDetail, OtherInstitutionDetailAdmin)# Other Institution details
admin.site.register(FileDetail, FileDetailAdmin)# File details
