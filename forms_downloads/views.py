from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

from admissions.models import PersonalDetail

def download_personal_details(request, user_id):
    personal_details = PersonalDetail.objects.get(user_id=user_id)

    # Create a BytesIO buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file"
    p = canvas.Canvas(buffer, pagesize=letter)

    # Set the font and font size for the PDF
    p.setFont("Helvetica", 12)

    # Draw the school logo in the header
    logo_path = 'static/images/logos/KAFU_LOGO.jpg'  # Replace with the actual path to the school logo
    logo_width = 100
    logo_height = 100
    logo_x = (letter[0] - logo_width) / 2  # Center horizontally
    logo_y = 650  # Adjust the vertical position as desired
    p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)

    # Set the header text
    text_y = 635
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, text_y, "KAIMOSI FRIENDS UNIVERSITY")
    p.setFont("Helvetica-Bold", 12)
    p.drawString(270, text_y-20, "Online Admission")

    # The student
    text_y = 570  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Student")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Username: {}".format(personal_details.user.username))


    # Write the personal details to the PDF
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Name")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Surname: {}              First Name: {}          Last Name: {}".format(personal_details.surname, personal_details.first_name, personal_details.last_name))

    # Gender section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Gender")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Date: {}             Gender: {}".format(personal_details.date, personal_details.gender))

    # Nationality section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Nationality")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "National ID: {}              Nationality: {}".format(personal_details.national_id, personal_details.nationality))

    # Address section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Address")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Email: {}                Phone: {}".format(personal_details.email, personal_details.phone))

    # Birth section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Birth")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "City: {}             Place of Birth: {}".format(personal_details.city, personal_details.pob))

    # Religion section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Religion")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Religion: {}".format(personal_details.religion))

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
