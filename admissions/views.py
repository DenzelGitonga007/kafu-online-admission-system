from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PersonalDetailForm, ParentDetailForm, SpouseDetailForm, NextKinDetailForm, HighSchoolDetailForm, EmergencyContactDetailForm, GamesDetailForm
from .models import PersonalDetail, ParentDetail, SpouseDetail, NextKinDetail, EmergencyContactDetail, GamesDetail
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
            messages.success(request, "Your personal details have been received successfully!!!\nNow fill in your parent(s) details in the form below")
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
            messages.success(request, "Your parent details have been received successfully!\nNow fill in your spouse details in the form below")
            return redirect('admissions:spouse_details')
         # If error in submission
        else:
            messages.error(request, 'There was an error while saving your parent details. Please try again.')
    else:
        form = ParentDetailForm()
    context = {'form': form}
    return render(request, 'admissions/parent_detail.html', context)


# Spouse details
@login_required
def spouse_detail_view(request):
    user = request.user
    if request.method == 'POST':
        form = SpouseDetailForm(request.POST)
        if form.is_valid():
            spouse_detail = form.save(commit=False)
            spouse_detail.user = user
            spouse_detail.save()
            # Success message
            messages.success(request, "Your spouse details have been received successfully!\nNow fill in your next of kin details in the form below")
            return redirect('admissions:next_kin_details')
        else:
            messages.error(request, 'There was an error while saving your parent details. Please try again.')
    else:
        form = SpouseDetailForm()
    context = {'form': form}
    return render(request, 'admissions/spouse_detail.html', context)

@login_required
def next_kin_detail_view(request):
    user = request.user
    if request.method == 'POST':
        form = NextKinDetailForm(request.POST)
        if form.is_valid():
            nxtk_detail = form.save(commit=False)
            nxtk_detail.user = user
            nxtk_detail.save()
            # Success message
            messages.success(request, "Your next of kin details have been received successfully!!!")
            return redirect('admissions:emergency_contact_details')
        else:
            messages.error(request, 'There was an error while saving your next of kin details. Please try again.')
    else:
        form = NextKinDetailForm()
    context = {'form': form}
    return render(request, 'admissions/nxtk_detail.html', context)


# Emergency contact    
@login_required
def emergency_contact_detail_view(request):
    user = request.user
    if request.method == 'POST':
        form = EmergencyContactDetailForm(request.POST)
        if form.is_valid():
            emergency_contact_detail = form.save(commit=False)
            emergency_contact_detail.user = user
            emergency_contact_detail.save()
            # Success message
            messages.success(request, "Your emergency contact details have been received successfully!\nNow fill in your high school(s) details in the form below")
            return redirect('admissions:high_school_details')
        else:
            messages.error(request, 'There was an error while saving your emergency contact details. Please try again.')
    else:
        form = EmergencyContactDetailForm()
    context = {'form': form}
    return render(request, 'admissions/emergency_contact_detail.html', context)

@login_required
def high_school_detail_view(request):
    user = request.user
    if request.method == 'POST':
        form = HighSchoolDetailForm(request.POST)
        if form.is_valid():
            high_school_detail = form.save(commit=False)
            high_school_detail.user = user
            high_school_detail.save()
            # Success message
            messages.success(request, "Your high school details have been received successfully!\nNow fill in your games and sports details in the form below")
            return redirect('admissions:games_details')
        else:
            messages.error(request, 'There was an error while saving your high school details. Please try again.')
    else:
        form = HighSchoolDetailForm()
    context = {'form': form}
    return render(request, 'admissions/high_school_detail.html', context)


@login_required
def games_detail_view(request):
    user = request.user
    if request.method == 'POST':
        form = GamesDetailForm(request.POST)
        if form.is_valid():
            games_detail = form.save(commit=False)
            games_detail.user = user
            games_detail.save()
            # Success message
            messages.success(request, "Your high school details have been received successfully!\nNow fill in your clubs and societies details in the form below")
            return redirect('home')
        else:
            messages.error(request, 'There was an error while saving your games details. Please try again.')
    else:
        form = GamesDetailForm()
    context = {'form': form}
    return render(request, 'admissions/games_detail.html', context)