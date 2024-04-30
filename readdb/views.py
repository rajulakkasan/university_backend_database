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