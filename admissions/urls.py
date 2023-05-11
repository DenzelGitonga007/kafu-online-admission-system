from django.urls import path
from . import views

app_name = 'admissions'

urlpatterns = [
    path('personal-details/', views.personal_detail_view, name='personal_details'),
]