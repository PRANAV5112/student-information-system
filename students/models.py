from django.db import models
from django.contrib.auth.models import User

# This is our existing Student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # We can add more student-specific fields here later, like 'enrollment_number'
    
    def __str__(self):
        return self.user.username

# This is our existing Parent model
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.user.username

#
# --- NEW GRADE MODEL ---
# (This is the new code you need)
#
class Grade(models.Model):
    # Link this grade to a specific student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    
    # These fields match your requirement for the new page
    year = models.CharField(max_length=100, help_text="e.g., 2024-2025")
    semester = models.CharField(max_length=10, help_text="e.g., IV")
    code = models.CharField(max_length=20, help_text="e.g., CS204")
    course = models.CharField(max_length=100, help_text="e.g., COMPUTER ORGANIZATION")
    units = models.IntegerField(default=0)
    grade = models.CharField(max_length=5, help_text="e.g., A+")
    
    # You also mentioned CGPA and Marks
    marks = models.CharField(max_length=10, blank=True, help_text="e.g., 95")
    cgpa = models.CharField(max_length=10, blank=True, help_text="e.g., 9.5")

    
    class Meta:
        # Ensure a student can't have the same course code twice
        unique_together = ('student', 'code')

    def __str__(self):
        return f"{self.student.user.username} - {self.code} ({self.grade})"