from django import forms
from .models import PersonalDetail, ParentDetail, SpouseDetail

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
