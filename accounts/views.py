from django.shortcuts import render, request
from  .forms import UserRegistrationForm

# Create your views here.

# Home view
def home(request):
    return render(request, 'accounts/home.html', context={})


# Creating the user
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home') # the home url pattern
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})