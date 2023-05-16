from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from admissions.models import PersonalDetail, ParentDetail, SpouseDetail, NextKinDetail, EmergencyContactDetail, HighSchoolDetail, GamesDetail, ClubsDetail, OtherInstitutionDetail, OtherDetail, FileDetail
from .forms import ViewPersonalDetailForm


def view_submitted_details(request):
    user = request.user

    # personal_details = PersonalDetail.objects.filter(user=user)
    parent_details = ParentDetail.objects.filter(user=user)
    spouse_details = SpouseDetail.objects.filter(user=user)
    next_kin_details = NextKinDetail.objects.filter(user=user)
    emergency_details = EmergencyContactDetail.objects.filter(user=user)
    high_school_details = HighSchoolDetail.objects.filter(user=user)
    games_details = GamesDetail.objects.filter(user=user)
    clubs_details = ClubsDetail.objects.filter(user=user)
    other_institution_details = OtherInstitutionDetail.objects.filter(user=user)
    other_details = OtherDetail.objects.filter(user=user)
    file_details = FileDetail.objects.filter(user=user)

    context = {
        # 'personal_details': personal_details,
        'parent_details': parent_details,
        'spouse_details': spouse_details,
        'next_kin_details': next_kin_details,
        'high_school_details': high_school_details,
        'games_details': games_details,
        'clubs_details': clubs_details,
        'other_institution_details': other_institution_details,
        'other_details': other_details,
        'file_details': file_details,
        }
    return render(request, 'submissions/view_details.html', context)

def view_personal_details(request, user_id):
    personal_detail = get_object_or_404(PersonalDetail, user_id=user_id)
    form = ViewPersonalDetailForm(instance=personal_detail)

    if request.method == 'POST':
        form = ViewPersonalDetailForm(request.POST, instance=personal_detail)
        if form.is_valid():
            form.save()
            return redirect('submissions:view_personal_details', user_id=user_id)

    context = {
        'form': form
    }
    return render(request, 'submissions/view_personal_details.html', context)