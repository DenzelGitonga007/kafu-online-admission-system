from django.urls import path
from . import views

app_name = 'admissions'

urlpatterns = [
    path('personal-details/', views.personal_detail_view, name='personal_details'), # personal details
    path('parent-details/', views.parent_detail_view, name='parent_details'), # parent details
    path('spouse-details/', views.spouse_detail_view, name='spouse_details'), #spouse details
    path('next-kin-details/', views.next_kin_detail_view, name='next_kin_details'), # next of kin details
    path('high-school-details/', views.high_school_detail_view, name="high_school_details"), # high school details
    path('emergency-contact-details/', views.emergency_contact_detail_view, name="emergency_contact_details"), # emergency contact details
    path('games-details/', views.games_detail_view, name="games_details"), # games details
    path('clubs-details/', views.clubs_detail_view, name="clubs_details"), # clubs details
]