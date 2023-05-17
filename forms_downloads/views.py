from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO

from admissions.models import PersonalDetail

def download_personal_details(request, user_id):
    personal_details = PersonalDetail.objects.get(user_id=user_id)

    # Create a BytesIO buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file"
    p = canvas.Canvas(buffer)

    # Set the font and font size for the PDF
    p.setFont("Helvetica", 12)

    # Write the personal details to the PDF
    # Name
    p.drawString(50, 700, "Surname: {}              First Name: {}          Last Name: {}".format(personal_details.surname, personal_details.first_name, personal_details.last_name))
    # Gender
    p.drawString(50, 640, "Date: {}             Gender: {}".format(personal_details.date, personal_details.gender))
    # Nationality
    p.drawString(50, 600, "National ID: {}              Nationality: {}".format(personal_details.national_id, personal_details.nationality))
    # Address
    p.drawString(50, 540, "Email: {}                Phone: {}".format(personal_details.email, personal_details.phone))
    # Birth
    p.drawString(50, 500, "City: {}             Place of Birth: {}".format(personal_details.city, personal_details.pob))
    p.drawString(50, 560, "Religion: {} ".format(personal_details.religion))

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Set the buffer's position back to the beginning
    buffer.seek(0)

    # Set the response headers for the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="personal_details.pdf"'

    # Write the buffer's content to the response
    response.write(buffer.getvalue())

    return response
