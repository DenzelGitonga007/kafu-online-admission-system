from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os

from admissions.models import PersonalDetail

from django.template.loader import get_template

def download_personal_details(request, user_id):
    # Retrieve the personal details form for the user
    personal_details = PersonalDetail.objects.get(user_id=user_id)

    # Generate a download file using a template
    template = get_template('forms_downloads/personal_details_template.txt')
    download_file = template.render({'personal_details': personal_details})

    # Create an HTTP response with the download file
    response = HttpResponse(download_file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="personal_details.txt"'
    return response

