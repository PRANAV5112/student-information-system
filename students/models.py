# students/models.py

# students/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    """
    Represents a student user. We link this to a User account.
    """
    # This creates a one-to-one link with Django's built-in User model.
    # Each User can only be one Student, and each Student must have one User account.
    # on_delete=models.CASCADE means if a User is deleted, their Student profile is also deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # You can add other student-specific fields here later, for example:
    # student_id = models.CharField(max_length=20, unique=True)
    # date_of_birth = models.DateField(null=True, blank=True)
    # grade = models.CharField(max_length=10, blank=True)

    def __str__(self):
        # This is how the object will be displayed in the admin panel.
        return self.user.username


class Parent(models.Model):
    """
    Represents a parent user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # A parent can be linked to one or more students.
    # A ManyToManyField is a good choice for this relationship.
    students = models.ManyToManyField(Student, blank=True)

    # You can add other parent-specific fields here later, for example:
    # phone_number = models.CharField(max_length=15, blank=True)
    # address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
