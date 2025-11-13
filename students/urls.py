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
    path('manage-grades/', views.manage_grades_view, name='manage_grades'),
    path('edit-grade/<int:grade_id>/', views.edit_grade_view, name='edit_grade'),
    path('delete-grade/<int:grade_id>/', views.delete_grade_view, name='delete_grade'),

]
