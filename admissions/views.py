from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PersonalDetailForm, ParentDetailForm
from .models import PersonalDetail, ParentDetail
from accounts.models import User

# Personal details
@login_required
def personal_detail_view(request):
    user = request.user
    if request.method == 'POST':
        form = PersonalDetailForm(request.POST)
        if form.is_valid():
            personal_detail = form.save(commit=False)
            personal_detail.user = user
            personal_detail.save()
            # Success message
            messages.success(request, "Your personal details have been received successfully!!!")
            return redirect('admissions:parent_details')
        # If error in submission
        else:
            messages.error(request, 'There was an error while saving your personal details. Please try again.')
    else:
        form = PersonalDetailForm()
    return render(request, 'admissions/personal_detail.html', {'form': form})

# Parent details
@login_required
def parent_detail_view(request):
    user = request.user
    if request.method == 'POST':
        form = ParentDetailForm(request.POST)
        if form.is_valid():
            parent_detail = form.save(commit=False)
            parent_detail.user = user
            parent_detail.save()
            # Success message
            messages.success(request, "Your parent details have been received successfully!!!")
            return redirect('home')
         # If error in submission
        else:
            messages.error(request, 'There was an error while saving your parent details. Please try again.')
    else:
        form = ParentDetailForm()
    context = {'form': form}
    return render(request, 'admissions/parent_detail.html', context)
