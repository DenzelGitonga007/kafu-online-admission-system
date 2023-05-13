from django.urls import path
from . import views

app_name = 'admissions'

urlpatterns = [
    path('personal-details/', views.personal_detail_view, name='personal_details'), # personal details
    path('parent-details/', views.parent_detail_view, name='parent_details'), # parent details
    path('spouse-details/', views.spouse_detail_view, name='spouse_details'), #spouse details
    path('next-kin/', views.next_kin_view, name='next_kin'), # next of kin details
]