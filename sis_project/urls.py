# sis_project/urls.py

from django.contrib import admin
# Make sure to import 'include'
from django.urls import path, include
from students import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Add this line to forward all requests on the main site
    # to your 'students' app's urls.py file.
    path('', include('students.urls')),
]
