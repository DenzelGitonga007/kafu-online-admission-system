from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

from admissions.models import PersonalDetail, ParentDetail, SpouseDetail, NextKinDetail, EmergencyContactDetail, HighSchoolDetail, GamesDetail

# Download personal details
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
    p.drawString(50, text_y, "Username: {}".format(personal_details.user.username))
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Personal Details Form")


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

# End of personal details

# Download parent details
def download_parent_details(request, user_id):
    parent_details = ParentDetail.objects.get(user_id=user_id)

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
    p.drawString(50, text_y, "Username: {}".format(parent_details.user.username))
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Parent Details Form")


    # Write the personal details to the PDF
    # Father
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Father")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Surname: {}              First Name: {}          Last Name: {}".format(parent_details.father_surname, parent_details.father_first_name, parent_details.father_last_name))

    # Nationality section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Nationality")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "National ID: {}              Occupation: {}".format(parent_details.father_national_id, parent_details.father_occupation))
    # End of Father

    # Mother
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Mother")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Surname: {}              First Name: {}          Last Name: {}".format(parent_details.mother_surname, parent_details.mother_first_name, parent_details.mother_last_name))

    # Nationality section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Nationality")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "National ID: {}              Occupation: {}".format(parent_details.mother_national_id, parent_details.mother_occupation))
    # End of Mother

    # Guardian
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Guardian")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Surname: {}              First Name: {}          Initial Name: {}".format(parent_details.guardian_surname, parent_details.guardian_first_name, parent_details.guardian_initial_name))

    # Nationality section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Nationality")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "National ID: {}              Occupation: {}".format(parent_details.guardian_national_id, parent_details.guardian_occupation))

    # Address section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Address")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Email: {}                Phone: {}".format(parent_details.guardian_email, parent_details.guardian_phone))

    # Birth section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Location")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "City: {}             P.O BOX: {}".format(parent_details.guardian_city, parent_details.guardian_pob))

    # End of Guardian

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Set the buffer's position back to the beginning
    buffer.seek(0)

    # Set the response headers for the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="parent_details.pdf"'

    # Write the buffer's content to the response
    response.write(buffer.getvalue())

    return response

# End of personal details

# Download spouse details
def download_spouse_details(request, user_id):
    spouse_details = SpouseDetail.objects.get(user_id=user_id)

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
    p.drawString(50, text_y, "Username: {}".format(spouse_details.user.username))
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Spouse Details Form")


    # Write the personal details to the PDF
    # Spouse
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Spouse")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Surname: {}              First Name: {}          Last Name: {}".format(spouse_details.spouse_surname, spouse_details.spouse_first_name, spouse_details.spouse_last_name))

    # Nationality section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Nationality")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "National ID: {}              Occupation: {}".format(spouse_details.spouse_national_id, spouse_details.spouse_occupation))
    
    # Address section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Address")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Email: {}                Phone: {}".format(spouse_details.spouse_email, spouse_details.spouse_phone))

    # Location section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Location")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "City: {}             P.O BOX: {}".format(spouse_details.spouse_city, spouse_details.spouse_pob))

    # End of Spouse

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Set the buffer's position back to the beginning
    buffer.seek(0)

    # Set the response headers for the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="spouse_details.pdf"'

    # Write the buffer's content to the response
    response.write(buffer.getvalue())

    return response

# End of Spouse details

# Download next of kin details
def download_next_kin_details(request, user_id):
    next_kin_details = NextKinDetail.objects.get(user_id=user_id)

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
    p.drawString(50, text_y, "Username: {}".format(next_kin_details.user.username))
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Next of Kin Details Form")


    # Write the personal details to the PDF
    # Next of Kin
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Next of Kin")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Surname: {}              First Name: {}          Initial Name: {}".format(next_kin_details.nxtk_surname, next_kin_details.nxtk_first_name, next_kin_details.nxtk_initial_name))

    # Nationality section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Nationality")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "National ID: {}              ".format(next_kin_details.nxtk_national_id))
    
    # Address section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Address")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Email: {}                Phone: {}".format(next_kin_details.nxtk_email, next_kin_details.nxtk_phone))

    # Location section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Location")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "City: {}             P.O BOX: {}".format(next_kin_details.nxtk_city, next_kin_details.nxtk_pob))

    # End of Next of Kin

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Set the buffer's position back to the beginning
    buffer.seek(0)

    # Set the response headers for the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Next of Kin Details.pdf"'

    # Write the buffer's content to the response
    response.write(buffer.getvalue())

    return response

# End of next of kin details

# Download emergency contact details
def download_emergency_contact_details(request, user_id):
    emergency_contact_details = EmergencyContactDetail.objects.get(user_id=user_id)

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
    p.drawString(50, text_y, "Username: {}".format(emergency_contact_details.user.username))
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Emergency Contact Details Form")


    # Write the personal details to the PDF
    # Next of Kin
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Emergency Contact")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Surname: {}              First Name: {}          Initial Name: {}".format(emergency_contact_details.emerge_con_surname, emergency_contact_details.emerge_con_first_name, emergency_contact_details.emerge_con_initial_name))

    # Nationality section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Nationality")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "National ID: {}              ".format(emergency_contact_details.emerge_con_national_id))
    
    # Address section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Address")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Email: {}                Phone: {}".format(emergency_contact_details.emerge_con_email, emergency_contact_details.emerge_con_phone))

    # Location section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Location")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "City: {}             P.O BOX: {}".format(emergency_contact_details.emerge_con_city, emergency_contact_details.emerge_con_pob))

    # End of Next of Kin

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Set the buffer's position back to the beginning
    buffer.seek(0)

    # Set the response headers for the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Emergency Contact Details.pdf"'

    # Write the buffer's content to the response
    response.write(buffer.getvalue())

    return response

# End of emergency contact details

# Download High School details
def download_high_school_details(request, user_id):
    high_school_details = HighSchoolDetail.objects.get(user_id=user_id)

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
    p.drawString(50, text_y, "Username: {}".format(high_school_details.user.username))
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "High School Details Form")


    # Write the personal details to the PDF
    # First High School
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "First High School")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Name: {}              Address: {}          Town: {}".format(high_school_details.first_high_school_name, high_school_details.first_high_school_address, high_school_details.first_high_school_town))

    # Date section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Dates of Learning")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "From: {}             To: {}".format(high_school_details.first_high_school_from_date, high_school_details.first_high_school_to_date))

    # End of first high school

    # Second High School
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Second High School")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Name: {}              Address: {}          Town: {}".format(high_school_details.second_high_school_name, high_school_details.second_high_school_address, high_school_details.second_high_school_town))

    # Date section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Dates of Learning")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "From: {}             To: {}".format(high_school_details.second_high_school_from_date, high_school_details.second_high_school_to_date))

    # End of second high school

    # Third high school
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Third High School")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Name: {}              Address: {}          Town: {}".format(high_school_details.third_high_school_name, high_school_details.third_high_school_address, high_school_details.third_high_school_town))

    # Date section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Dates of Learning")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "From: {}             To: {}".format(high_school_details.third_high_school_from_date, high_school_details.third_high_school_to_date))

    # End of first high school

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Set the buffer's position back to the beginning
    buffer.seek(0)

    # Set the response headers for the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="High School Details.pdf"'

    # Write the buffer's content to the response
    response.write(buffer.getvalue())

    return response

# End of High School details


# Download Games and Sports details
def download_games_details(request, user_id):
    games_details = GamesDetail.objects.get(user_id=user_id)

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
    p.drawString(50, text_y, "Username: {}".format(games_details.user.username))
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Games Details Form")


    # Write the personal details to the PDF
    # First High School
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Games and Sports")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Played: {}".format(games_details.games_and_sports))

    # Date section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Games Representations")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Represented: {}".format(games_details.games_representation))

    # End of games and sports

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Set the buffer's position back to the beginning
    buffer.seek(0)

    # Set the response headers for the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Games and Sports Details.pdf"'

    # Write the buffer's content to the response
    response.write(buffer.getvalue())

    return response

# End of Games and Sport details


# Download Clubs and Societies

def download_clubs_details(request, user_id):
    high_school_details = HighSchoolDetail.objects.get(user_id=user_id)

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
    p.drawString(50, text_y, "Username: {}".format(high_school_details.user.username))
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "High School Details Form")


    # Write the personal details to the PDF
    # First High School
    # Name section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "First High School")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Name: {}              Address: {}          Town: {}".format(high_school_details.first_high_school_name, high_school_details.first_high_school_address, high_school_details.first_high_school_town))

    # Date section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Dates of Learning")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "From: {}             To: {}".format(high_school_details.first_high_school_from_date, high_school_details.first_high_school_to_date))

    # End of first high school

    # Second High School
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Second High School")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Name: {}              Address: {}          Town: {}".format(high_school_details.second_high_school_name, high_school_details.second_high_school_address, high_school_details.second_high_school_town))

    # Date section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Dates of Learning")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "From: {}             To: {}".format(high_school_details.second_high_school_from_date, high_school_details.second_high_school_to_date))

    # End of second high school

    # Third high school
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Third High School")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "Name: {}              Address: {}          Town: {}".format(high_school_details.third_high_school_name, high_school_details.third_high_school_address, high_school_details.third_high_school_town))

    # Date section heading
    text_y -= 70  # Adjust the vertical position as desired
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, text_y, "Dates of Learning")
    p.setFont("Helvetica", 12)
    p.drawString(50, text_y - 20, "From: {}             To: {}".format(high_school_details.third_high_school_from_date, high_school_details.third_high_school_to_date))

    # End of first high school

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Set the buffer's position back to the beginning
    buffer.seek(0)

    # Set the response headers for the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="High School Details.pdf"'

    # Write the buffer's content to the response
    response.write(buffer.getvalue())

    return response

# End of High School details

