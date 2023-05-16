from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from admissions.models import PersonalDetail, ParentDetail, SpouseDetail, NextKinDetail, EmergencyContactDetail, HighSchoolDetail, GamesDetail, ClubsDetail, OtherInstitutionDetail, OtherDetail, FileDetail
from .forms import ViewPersonalDetailForm, ViewParentDetailForm, ViewSpouseDetailForm, ViewNextKinDetailForm, ViewEmergencyContactDetailForm, ViewHighSchoolDetailForm

@login_required
def view_submitted_details(request):
    user = request.user

    
    emergency_details = EmergencyContactDetail.objects.filter(user=user)
    high_school_details = HighSchoolDetail.objects.filter(user=user)
    games_details = GamesDetail.objects.filter(user=user)
    clubs_details = ClubsDetail.objects.filter(user=user)
    other_institution_details = OtherInstitutionDetail.objects.filter(user=user)
    other_details = OtherDetail.objects.filter(user=user)
    file_details = FileDetail.objects.filter(user=user)

    context = {
        
        'high_school_details': high_school_details,
        'games_details': games_details,
        'clubs_details': clubs_details,
        'other_institution_details': other_institution_details,
        'other_details': other_details,
        'file_details': file_details,
        }
    return render(request, 'submissions/view_details.html', context)


# Personal details
@login_required
def view_personal_details(request, user_id):
    personal_detail = get_object_or_404(PersonalDetail, user_id=user_id)
    form = ViewPersonalDetailForm(instance=personal_detail)

    if request.method == 'POST':
        form = ViewPersonalDetailForm(request.POST, instance=personal_detail)
        if form.is_valid():
            form.save()
            # Success message
            messages.success(request, "Your personal details have been updated successfully!!! See the details below")
            return redirect('submissions:view_personal_details', user_id=user_id)

    context = {
        'form': form
    }
    return render(request, 'submissions/view_personal_details.html', context)

# Parent details
@login_required
def view_parent_details(request, user_id):
    parent_detail = get_object_or_404(ParentDetail, user_id=user_id)
    form = ViewParentDetailForm(instance=parent_detail)

    if request.method == 'POST':
        form = ViewParentDetailForm(request.POST, instance=parent_detail)
        if form.is_valid():
            form.save()
            # Success message
            messages.success(request, "Your parent details have been updated successfully!!! See the details below")
            return redirect('submissions:view_parent_details', user_id=user_id)

    context = {
        'form': form
    }
    return render(request, 'submissions/view_parent_details.html', context)

# Spouse details
@login_required
def view_spouse_details(request, user_id):
    spouse_detail = get_object_or_404(SpouseDetail, user_id=user_id)
    form = ViewSpouseDetailForm(instance=spouse_detail)

    if request.method == 'POST':
        form = ViewSpouseDetailForm(request.POST, instance=spouse_detail)
        if form.is_valid():
            form.save()
            # Success message
            messages.success(request, "Your spouse details have been updated successfully!!! See the details below")
            return redirect('submissions:view_spouse_details', user_id=user_id)

    context = {
        'form': form
    }
    return render(request, 'submissions/view_spouse_details.html', context)

# Next of kin details
@login_required
def view_next_kin_details(request, user_id):
    next_kin_detail = get_object_or_404(NextKinDetail, user_id=user_id)
    form = ViewNextKinDetailForm(instance=next_kin_detail)

    if request.method == 'POST':
        form = ViewNextKinDetailForm(request.POST, instance=next_kin_detail)
        if form.is_valid():
            form.save()
            # Success message
            messages.success(request, "Your next of kin details have been updated successfully!!! See the details below")
            return redirect('submissions:view_next_kin_details', user_id=user_id)

    context = {
        'form': form
    }
    return render(request, 'submissions/view_next_kin_details.html', context)

# Emergency contact details
@login_required
def view_emergency_contact_details(request, user_id):
    emergency_contact_detail = get_object_or_404(EmergencyContactDetail, user_id=user_id)
    form = ViewEmergencyContactDetailForm(instance=emergency_contact_detail)

    if request.method == 'POST':
        form = ViewEmergencyContactDetailForm(request.POST, instance=emergency_contact_detail)
        if form.is_valid():
            form.save()
            # Success message
            messages.success(request, "Your emergency contact details have been updated successfully!!! See the details below")
            return redirect('submissions:view_emergency_contact_details', user_id=user_id)

    context = {
        'form': form
    }
    return render(request, 'submissions/view_emergency_contact_details.html', context)

# High school details
@login_required
def view_high_school_details(request, user_id):
    high_school_detail = get_object_or_404(HighSchoolDetail, user_id=user_id)
    form = ViewHighSchoolDetailForm(instance=high_school_detail)

    if request.method == 'POST':
        form = ViewHighSchoolDetailForm(request.POST, instance=high_school_detail)
        if form.is_valid():
            form.save()
            # Success message
            messages.success(request, "Your high school details have been updated successfully!!! See the details below")
            return redirect('submissions:view_high_school_details', user_id=user_id)

    context = {
        'form': form
    }
    return render(request, 'submissions/view_high_school_details.html', context)