from django import forms
from .models import PersonalDetail, ParentDetail, SpouseDetail, NextKinDetail, HighSchoolDetail, EmergencyContactDetail,GamesDetail

# Personal details
class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        fields = [
            'surname', 
            'first_name', 
            'last_name', 
            'date', 
            'gender', 
            'national_id', 
            'nationality', 
            'religion', 
            'email', 
            'phone', 
            'city', 
            'pob'
        ]

# Parent details
class ParentDetailForm(forms.ModelForm):
    class Meta:
        model = ParentDetail
        fields = [
            # Father
            'father',
            'father_surname',
            'father_first_name',
            'father_last_name',
            'father_national_id',
            'father_occupation',
            
            # Mother
            'mother',
            'mother_surname',
            'mother_first_name',
            'mother_last_name',
            'mother_national_id',
            'mother_occupation',

            # Guardian
            'guardian_surname',
            'guardian_first_name',
            'guardian_initial_name',
            'guardian_national_id',
            'guardian_email',
            'guardian_phone',
            'guardian_city',
            'guardian_pob',
            'guardian_occupation',

        ]

class SpouseDetailForm(forms.ModelForm):
    class Meta:
        model = SpouseDetail
        fields = [
            'marital_status',
            'spouse_surname',
            'spouse_first_name',
            'spouse_last_name',
            'spouse_national_id',
            'spouse_email',
            'spouse_phone',
            'spouse_city',
            'spouse_pob',
            'spouse_occupation',
        ]

# Next of kin details
class NextKinDetailForm(forms.ModelForm):
    class Meta:
        model = NextKinDetail
        fields = [
            'nxtk_surname',
            'nxtk_first_name',
            'nxtk_initial_name',
            'nxtk_national_id',
            'nxtk_email',
            'nxtk_phone',
            'nxtk_city',
            'nxtk_pob',
        ]

# High School details
class HighSchoolDetailForm(forms.ModelForm):
    class Meta:
        model = HighSchoolDetail
        fields = [
            # First High School
            'first_high_school_name',
            'first_high_school_address',
            'first_high_school_town',
            'first_high_school_from_date',
            'first_high_school_to_date',

            # Second High School
            'second_high_school_name',
            'second_high_school_address',
            'second_high_school_town',
            'second_high_school_from_date',
            'second_high_school_to_date',

            # Third High School
            'third_high_school_name',
            'third_high_school_address',
            'third_high_school_town',
            'third_high_school_from_date',
            'third_high_school_to_date',
        ]

# Emergency Contact Details
class EmergencyContactDetailForm(forms.ModelForm):
    class Meta:
        model = EmergencyContactDetail
        fields = [
            'emerge_con_surname',
            'emerge_con_first_name',
            'emerge_con_initial_name',
            'emerge_con_national_id',
            'emerge_con_email',
            'emerge_con_phone',
            'emerge_con_city',
            'emerge_con_pob',
            # 'emerge_con_occupation',
        ]


# Games Detail
class GamesDetailForm(forms.ModelForm):
    class Meta:
        model = GamesDetail
        fields = [
            'games_and_sports',
            'games_representation',
        ]