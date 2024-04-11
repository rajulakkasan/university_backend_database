from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # User id - unique field mapping to every user
    user_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

class Admin(CustomUser):from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length=50, unique=True)  # Use ID field as unique identifier
    

    def __str__(self):
        return self.username

class Admin(CustomUser):
    pass

class Professor(CustomUser):
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    

class Student(CustomUser):
    enrolled_courses = models.ManyToManyField('Course', related_name='students')
    pass

class Professor(CustomUser):
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Student(CustomUser):
    enrolled_courses = models.ManyToManyField('Course', related_name='students')
