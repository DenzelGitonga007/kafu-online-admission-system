from django.urls import path
from . import views
app_name = 'forms_downloads'

urlpatterns = [
    path('download_personal_details/<int:user_id>/', views.download_personal_details, name='download_personal_details'),
]