# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # This line maps the root URL ('') to the login_view function
    # from your students/views.py file.
     # This path handles the login page at the root URL.
    path('', views.login_view, name='login'),
    
    # This is the new path for the dashboard page.
    # The name='dashboard' is what fixes the NoReverseMatch error.
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # This path is for the logout functionality.
    path('logout/', views.logout_view, name='logout'),
]
