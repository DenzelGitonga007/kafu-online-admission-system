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
]