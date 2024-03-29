from django.urls import path

from . import views


app_name = 'submissions'

urlpatterns = [
    path('view-details/', views.view_submitted_details, name='view_details'),
    path('personal-details/<int:user_id>/', views.view_personal_details, name='view_personal_details'), # personal details
    path('parent-details/<int:user_id>/', views.view_parent_details, name="view_parent_details"), # parent details
    path('spouse-details/<int:user_id>/', views.view_spouse_details, name="view_spouse_details"), # spouse details
    path('next-kin-details/<int:user_id>/', views.view_next_kin_details, name="view_next_kin_details"), # next of kin details
    path('emergency-contact-details/<int:user_id>/', views.view_emergency_contact_details, name="view_emergency_contact_details"), # next of kin details
    path('high-school-details/<int:user_id>/', views.view_high_school_details, name="view_high_school_details"), # high school details
    path('games-and-sports-details/<int:user_id>/', views.view_games_details, name="view_games_details"), # games details
    path('clubs-and-societies-details/<int:user_id>/', views.view_clubs_details, name="view_clubs_details"), # clubs details
    path('other-institution-details/<int:user_id>/', views.view_other_institution_details, name="view_other_institution_details"), # other institution details
    path('other-details/<int:user_id>/', views.view_other_details, name="view_other_details"), # other institution details
    path('file-details/<int:user_id>/', views.view_file_details, name="view_file_details"), # file details

]
