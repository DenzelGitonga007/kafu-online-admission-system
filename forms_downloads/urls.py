from django.urls import path
from . import views
app_name = 'forms_downloads'

urlpatterns = [
    path('download-personal-details/<int:user_id>/', views.download_personal_details, name='download_personal_details'), # personal details download
    path('download-parent-details/<int:user_id>/', views.download_parent_details, name='download_parent_details'), # personal details download
    path('download-spouse-details/<int:user_id>/', views.download_spouse_details, name='download_spouse_details'), # personal details download
    path('download-next-kin-details/<int:user_id>/', views.download_next_kin_details, name='download_next_kin_details'), # personal details download
    path('download-emergency-contact_details/<int:user_id>/', views.download_emergency_contact_details, name='download_emergency_contact_details'), # emergency contact details download
    path('download-high-school-details/<int:user_id>/', views.download_high_school_details, name='download_high_school_details'), # high school details download
    path('download-games-and-sport-details/<int:user_id>/', views.download_games_details, name='download_games_details'), # games and sports details download
    path('download-clubs-and-societies-details/<int:user_id>/', views.download_clubs_details, name='download_clubs_details'), # clubs and societies details download
    path('download-other-institution-details/<int:user_id>/', views.download_other_institution_details, name='download_other_institution_details'), # clubs and societies details download
    path('download-other-details/<int:user_id>/', views.download_other_details, name='download_other_details'), # clubs and societies details download
]