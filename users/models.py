from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length=50, unique=True)  # Use ID field as unique identifier
    # Add any other common fields

    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    dept_name = models.CharField(max_length=100)
    tot_cred = models.IntegerField()

    def __str__(self):
        return self.user.username  # Return the username as the string representation

class Professor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    dept_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username  # Return the username as the string representation
