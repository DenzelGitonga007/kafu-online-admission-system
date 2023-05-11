from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# For the custom user
from django.conf import settings
# Create your models here.

# The student themselves, and pick the current signed in user
class StudentManager(models.Manager):
    def create_from_user(self, user):
        student = self.create(user=user)
        return student
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')

    objects = StudentManager()

    def __str__(self):
        return f"{self.get_username()} - {self.user.full_name}"
        # return f"{self.username} - {self.email}"
    
    def get_username(self):
        return self.user.username

# Personal details
class PersonalDetail(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField()
    gender = models.CharField(max_length=50)
    national_id = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pob = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.surname} - {self.first_name}"
        # return f"{self.username} - {self.email}"
