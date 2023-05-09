from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User

class UserRegistrationForm(UserCreationForm):
    # username comes by default
    email = forms.EmailField(required=True)
    full_name = forms.CharField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user