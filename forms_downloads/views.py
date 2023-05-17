from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings
import os
from reportlab.pdfgen import canvas

from admissions.models import PersonalDetail

def download_personal_details(request, user_id):
    # Retrieve the personal details form for the user
    personal_details = get_object_or_404(PersonalDetail, user_id=user_id)

    # Create a PDF file using ReportLab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="personal_details.pdf"'

    # Create the PDF document
    p = canvas.Canvas(response)

    # Write the form data to the PDF document
    p.drawString(100, 700, f"First Name: {personal_details.first_name}")
    p.drawString(100, 670, f"Last Name: {personal_details.last_name}")
    # Add more fields as needed

    # Save the PDF document
    p.showPage()
    p.save()

    return response
