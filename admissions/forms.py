from django import forms
from .models import PersonalDetail
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
            'pob']