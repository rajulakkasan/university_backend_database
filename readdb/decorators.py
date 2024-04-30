from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from functools import wraps

def prevent_logged_in_users(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # If user is logged in, redirect to some other page like home
            return redirect('home')
        else:
            # If user is not logged in, proceed with the view function
            return view_func(request, *args, **kwargs)
    return _wrapped_view

from functools import wraps
from django.shortcuts import redirect

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if the user has the required user type
            if hasattr(request.user, 'user_type') and request.user.user_type == 'admin':
                # Proceed with the view function if the conditions are met
                return view_func(request, *args, **kwargs)
            else:
                # Redirect to unauthorized page if user is authenticated but not an admin
                return redirect('unauthorized')
        else:
            # Redirect to login page if user is not authenticated
            return redirect('login')
    return _wrapped_view


def professor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated
        print(request.user)
        if request.user.is_authenticated:
            # Check if the user has the required user type
            if hasattr(request.user, 'user_type') and request.user.user_type == 'professor':
                # Proceed with the view function if the conditions are met
                return view_func(request, *args, **kwargs)
            else:
                # Redirect to unauthorized page if user is authenticated but not an admin
                return redirect('unauthorized')
        else:
            # Redirect to login page if user is not authenticated
            return redirect('login')
    return _wrapped_view

def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check if the user has the required user type
            if hasattr(request.user, 'user_type') and request.user.user_type == 'student':
                # Proceed with the view function if the conditions are met
                return view_func(request, *args, **kwargs)
            else:
                # Redirect to unauthorized page if user is authenticated but not an admin
                return redirect('unauthorized')
        else:
            # Redirect to login page if user is not authenticated
            return redirect('login')
    return _wrapped_view
