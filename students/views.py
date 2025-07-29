# students/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Student, Parent
from django.contrib.auth.decorators import login_required

def login_view(request):
    """
    Handles the login process for both Students and Parents.
    """
    if request.method == 'POST':
        # Get data from the form
        login_id = request.POST.get('login_id')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Authenticate the user
        user = authenticate(request, username=login_id, password=password)

        if user is not None:
            # Check if the user type matches the selection
            if user_type == 'student' and hasattr(user, 'student'):
                login(request, user)
                return redirect('dashboard')
            elif user_type == 'parent' and hasattr(user, 'parent'):
                login(request, user)
                return redirect('dashboard')
            else:
                # User exists but selected the wrong profile type
                messages.error(request, 'Invalid user type selected for this account.')
        else:
            # Invalid credentials
            messages.error(request, 'Invalid LOGIN ID or Password.')

    # If a GET request or login failed, render the login page
    return render(request, 'login.html')


@login_required
def dashboard_view(request):
    """
    A simple dashboard page for logged-in users.
    """
    user_type = None
    if hasattr(request.user, 'student'):
        user_type = 'Student'
    elif hasattr(request.user, 'parent'):
        user_type = 'Parent'
    
    context = {
        'user_type': user_type
    }
    return render(request, 'dashboard.html', context)


def logout_view(request):
    """
    Logs the user out.
    """
    logout(request)
    return redirect('login')

