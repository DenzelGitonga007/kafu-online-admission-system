from django.urls import path
from . import views
app_name = 'forms_downloads'

urlpatterns = [
    path('download_personal_details/<int:user_id>/', views.download_personal_details, name='download_personal_details'), # personal details download
    path('download_parent_details/<int:user_id>/', views.download_parent_details, name='download_parent_details'), # personal details download
]