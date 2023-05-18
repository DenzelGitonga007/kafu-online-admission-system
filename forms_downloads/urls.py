from django.urls import path
from . import views
app_name = 'forms_downloads'

urlpatterns = [
    path('download_personal_details/<int:user_id>/', views.download_personal_details, name='download_personal_details'), # personal details download
    path('download_parent_details/<int:user_id>/', views.download_parent_details, name='download_parent_details'), # personal details download
    path('download_spouse_details/<int:user_id>/', views.download_spouse_details, name='download_spouse_details'), # personal details download
    path('download_next_kin_details/<int:user_id>/', views.download_next_kin_details, name='download_next_kin_details'), # personal details download
]