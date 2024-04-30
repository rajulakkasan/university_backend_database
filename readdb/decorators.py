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

