from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import PersonalDetailForm
from .models import Student, PersonalDetail

@login_required
def personal_detail_view(request):
    if request.method == 'POST':
        form = PersonalDetailForm(request.POST)
        if form.is_valid():
            personal_detail = form.save(commit=FALSE)
            student = Student.objects.get(user=request.user)
            persona_detail.student = student
            personal_detail.save()
            return redirect('home')
    else:
        form = PersonalDetailForm()
    return render(request, 'admissions/personal_detail.html', {'form': form})