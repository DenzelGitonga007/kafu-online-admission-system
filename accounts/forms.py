from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User

class UserRegistrationForm(UserCreationForm):
    # username
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.fullname = self.fullname['fullname']
        user.phone_number = self.phone_number['phone_number']
        if commit:
            save()
        return user