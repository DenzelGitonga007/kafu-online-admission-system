from django.urls import path

from . import views


app_name = 'submissions'

urlpatterns = [
    path('view-details/', views.view_submitted_details, name='view_details'),
    path('personal-details/<int:user_id>/', views.view_personal_details, name='view_personal_details'),
]
