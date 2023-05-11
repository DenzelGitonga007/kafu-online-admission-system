from django.urls import path
from . import views
urlpatterns = [
    path('', views.personal_detail_view, name='personal_details'),
]