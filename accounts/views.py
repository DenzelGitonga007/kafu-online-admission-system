from django.shortcuts import render, redirect
from  .forms import UserRegistrationForm
# To display message
from django.contrib import messages

# Create your views here.

# Home view
def home(request):
    return render(request, 'accounts/home.html', context={})


# Creating the user
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Success message
            messages.success(request, "Congratulations! You have created an account successfully")
            return redirect('home') # the home url pattern
        # If error in creation
        else:
            messages.error(request, 'There was an error while creating your account. Please try again.')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})