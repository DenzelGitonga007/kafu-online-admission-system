from django.urls import path

from . import views


app_name = 'submissions'

urlpatterns = [
    path('view-details/', views.view_submitted_details, name='view_details'),
    path('personal-details/<int:user_id>/', views.view_personal_details, name='view_personal_details'), # personal details
    path('parent-details/<int:user_id>/', views.view_parent_details, name="view_parent_details"), # parent details
    path('spouse-details/<int:user_id>/', views.view_spouse_details, name="view_spouse_details"), # spouse details
]
