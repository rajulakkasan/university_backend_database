from django.db import models
from django.contrib.auth.models import AbstractUser



class Department(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    building = models.CharField(max_length=32, blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=32)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  
    total_credits = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name}"


class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=64, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses', null=True)
    credits = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Instructor(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=32, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Prerequisite(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prerequisites')
    prerequisite_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='dependent_courses')

    def __str__(self):
        return f"{self.course} -> {self.prerequisite_course}"


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=4)
    semester = models.IntegerField()
    year = models.IntegerField()
    building = models.CharField(max_length=32, null=True, blank=True)
    room = models.CharField(max_length=8, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ['course', 'section_name', 'semester', 'year']


class Teaches(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='XXXXX')
    semester = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        unique_together = ['course', 'section', 'semester', 'year', 'instructor']


class Takes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=99999) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default='XXXXX') 
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=1)  
    semester = models.IntegerField(default=1)  
    year = models.IntegerField(default=2024)  
    grade = models.CharField(max_length=2, default='B')

    class Meta:
        unique_together = ['student', 'course', 'section', 'semester', 'year']


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('professor', 'Professor'),
        ('student', 'Student'),
    ]

    user_type = models.CharField(
        max_length=25,
        choices=USER_TYPE_CHOICES,
        default='student'
    )

class Publication(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return self.title

class FundingSecured(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    academic_year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return f"${self.amount} secured"