from django.db import models
from django.http import HttpResponse, JsonResponse
from readdb.models import Department, Course, Instructor, Student, Prerequisite, Section, Takes, Teaches, FundingSecured, Publication, User
from django.db.models import Min, Max, Avg, Sum, Count

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import admin_required, professor_required, student_required, prevent_logged_in_users
from .forms import UserRegistrationForm

import logging
from .forms import UserLoginForm
from .authentication_backends import CustomAuthBackend

logger = logging.getLogger(__name__)

@admin_required
# FEATURE ------  F1  -------------------
def roster_view(request):
    # Get professors from the database
    professors = Instructor.objects.all()
    
    # Sort professors based on selected criteria (assuming 'sort' is passed via GET request)
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        professors = professors.order_by('name')
    elif sort_by == 'department':
        professors = professors.order_by('department')
    elif sort_by == 'salary':
        professors = professors.order_by('salary')

    # Render the template with the sorted professors
    return render(request, 'roster.html', {'professors': professors})

@admin_required
# FEATURE ------  F2  -------------------
def salary_view(request):
    print(request.user)
    # Fetching data using Django ORM
    salary_data = Instructor.objects.values('department').annotate(
        min_salary=Min('salary'),
        max_salary=Max('salary'),
        avg_salary=Avg('salary')
    )

    return render(request, 'salary.html', {'salary_data': salary_data})


# # Define a dictionary to map numerical semester values to semester names
# SEMESTER_MAP = {
#     '1': 'Spring',
#     '2': 'Summer',
#     '3': 'Fall',
# }
@admin_required
# FEATURE ------  F3  -------------------
def performance_view(request):
    if request.method == 'POST':
        # Get professor's name, academic year, and semester from the request
        professor_name = request.POST.get('professor_name')
        academic_year = request.POST.get('academic_year')
        semester_number = request.POST.get('semester')

        # Retrieve the professor object based on the provided name
        professor = get_object_or_404(Instructor, name=professor_name)
        
        

        # Calculate the number of course sections taught by the professor during the semester
        course_sections_taught = Section.objects.filter(teaches__instructor=professor, semester=semester_number, year=academic_year).count()
        
        # Calculate the number of students taught by the professor
        students_taught = Takes.objects.filter(section__teaches__instructor=professor, semester=semester_number, year=academic_year).count()

        # Calculate the total dollar amount of funding secured by the professor
        total_funding_secured = FundingSecured.objects.filter(instructor=professor, semester=semester_number, academic_year=academic_year).aggregate(total_amount=Sum('amount'))['total_amount'] or 0

        # Calculate the total number of papers published by the professor
        total_papers_published = Publication.objects.filter(instructor=professor, semester=semester_number, publication_year=academic_year).count()

        # Construct the context to pass to the template
        context = {
            'professor_name': professor_name,
            'academic_year': academic_year,
            'semester': semester_number,
            'course_sections_taught': course_sections_taught,
            'students_taught': students_taught,
            'total_funding_secured': total_funding_secured,
            'total_papers_published': total_papers_published
        }

        return render(request, 'performance.html', context)

    return render(request, 'performance.html')

@professor_required
# FEATURE ------  F4  -------------------
def course_sections_view(request):
    if request.method == 'POST':
        # Get professor's name and semester from the request
        professor_name = request.POST.get('professor_name')
        semester_number = request.POST.get('semester')

        # Retrieve the professor object based on the provided name
        professor = get_object_or_404(Instructor, name=professor_name)

        # Retrieve course sections taught by the professor in the chosen semester
        sections_taught = Section.objects.filter(teaches__instructor=professor, semester=semester_number)

        # Retrieve the number of students enrolled in each section
        sections_with_students = []
        for section in sections_taught:
            # Count the number of students enrolled in the section
            num_students = Takes.objects.filter(section=section).count()
            # Append section details along with the student count to the list
            sections_with_students.append({
                'course': section.course,
                'section_name': section.section_name,
                'semester': section.semester,
                'year': section.year,
                'num_students': num_students
            })

        # Construct the context to pass to the template
        context = {
            'professor_name': professor_name,
            'semester': semester_number,
            'sections_with_students': sections_with_students
        }

        return render(request, 'course_sections.html', context)

    return render(request, 'course_sections.html')


@professor_required
# FEATURE ------  F5  -------------------
def enrolled_students_view(request):
    if request.method == 'POST':
        # Get professor's name and semester from the request
        professor_name = request.POST.get('professor_name')
        semester_number = request.POST.get('semester')

        # Retrieve the professor object based on the provided name
        professor = get_object_or_404(Instructor, name=professor_name)

        # Retrieve course sections taught by the professor in the chosen semester
        sections_taught = Section.objects.filter(teaches__instructor=professor, semester=semester_number)

        enrolled_students = []
        for section in sections_taught:
            # Get the list of students enrolled in the section
            students_enrolled = Takes.objects.filter(section=section)
            for student_enrolled in students_enrolled:
                enrolled_students.append(student_enrolled.student)

        # Construct the context to pass to the template
        context = {
            'professor_name': professor_name,
            'semester': semester_number,
            'enrolled_students': enrolled_students
        }

        return render(request, 'enrolled_students.html', context)

    return render(request, 'enrolled_students.html')

@student_required
# FEATURE ------  F6  -------------------
def dept_sections_view(request):
    if request.method == 'POST':
        # Get department name, year, and semester from the request
        department_name = request.POST.get('department_name')
        year = request.POST.get('year')
        semester = request.POST.get('semester')

        # Query course sections offered by the chosen department in the chosen year and semester
        course_sections = Section.objects.filter(course__department__name=department_name, year=year, semester=semester)

        # Construct the context to pass to the template
        context = {
            'department_name': department_name,
            'year': year,
            'semester': semester,
            'course_sections': course_sections
        }

        return render(request, 'dept_sections.html', context)

    return render(request, 'dept_sections.html')


def home_view(request):
    if request.user.is_authenticated:
        
        print(request.user)
        user_type = request.user.user_type  
        print(user_type)
        
        if user_type == 'admin':
            return redirect('roster') 
        elif user_type == 'professor':
            return redirect('course_sections')  # Replace 'instructor_home' with the URL name of the instructor home page
        elif user_type == 'student':
            return redirect('dept_sections')  # Replace 'student_home' with the URL name of the student home page
        # Add more conditions for other user types as needed
        else:
            # Handle other user types or edge cases
            return redirect('unauthorized')  # Redirect to unauthorized page if user type is not recognized
    else:
        return redirect('login')  # Redirect to login page if user is not authenticated

@prevent_logged_in_users
def login_view(request):
    print("User : ",request.user)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        
        print("#####1#####",request.session.items())
        user = authenticate(request, username=username, password=password)
        print("#####2#####",request.session.items())
        print(user)
        if user is not None:
            print("Hello Bhanu Printing again, user :",user)
            login(request, user)
            print("#####3#####",request.session.items())
            # for attr in dir(user):
            #     if not attr.startswith('_') and not hasattr(user.__class__, attr):
            #         value = getattr(user, attr)
            #         print(f"{attr}: {value}")
            messages.success(request, 'You have successfully logged in.')
            return redirect('roster')  # Redirect to the home page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@prevent_logged_in_users
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def unauthorized_view(request):
    return render(request, 'unauthorized.html') 