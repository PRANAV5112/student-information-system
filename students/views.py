from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, Parent, Grade 

# This view is correct and unchanged
def login_view(request):
    """
    Handles the login process for both Students and Parents.
    """
    if request.method == 'POST':
        login_id = request.POST.get('login_id')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        user = authenticate(request, username=login_id, password=password)

        if user is not None:
            if user_type == 'student' and hasattr(user, 'student'):
                login(request, user)
                return redirect('dashboard')
            elif user_type == 'parent' and hasattr(user, 'parent'):
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid user type selected for this account.')
        else:
            messages.error(request, 'Invalid LOGIN ID or Password.')

    return render(request, 'login.html')

# This view is correct and unchanged
@login_required
def dashboard_view(request):
    """
    Displays the dashboard.
    If the user is a student, it fetches their grades.
    """
    user_type = None
    grades = []  # Initialize an empty list for grades

    if hasattr(request.user, 'student'):
        user_type = 'Student'
        # Fetch all grades that belong to this specific student
        grades = Grade.objects.filter(student=request.user.student).order_by('year', 'semester')
        
    elif hasattr(request.user, 'parent'):
        user_type = 'Parent'
        # Later, we could fetch grades for all linked children
    
    context = {
        'user_type': user_type,
        'grades': grades  # Pass the grades to the dashboard template
    }
    return render(request, 'dashboard.html', context)

# This view is correct and unchanged
def logout_view(request):
    """
    Logs the user out.
    """
    logout(request)
    return redirect('login')

# This view is slightly improved with better error handling and feedback
@login_required
def manage_grades_view(request):
    """
    Displays the form to add a new grade and a list of all existing grades.
    Only accessible by staff users.
    """
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('dashboard')

    if request.method == 'POST':
        student_id = request.POST.get('student')
        
        # --- IMPROVED ERROR HANDLING ---
        # Use get_object_or_404 to prevent a server crash
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            messages.error(request, "The selected student does not exist.")
            return redirect('manage_grades')
        # --- END OF IMPROVEMENT ---

        code = request.POST.get('code')

        # --- THIS IS THE NEW CODE THAT FIXES YOUR ERROR ---
        # It checks for duplicates before trying to create.
        if Grade.objects.filter(student=student, code=code).exists():
            messages.error(request, f"A grade for '{student.user.username}' with course code '{code}' already exists. Please use the 'Edit' button instead.")
            return redirect('manage_grades')
        # --- END OF NEW CODE ---

        year = request.POST.get('year')
        semester = request.POST.get('semester')
        code = request.POST.get('code')
        course = request.POST.get('course')
        units = request.POST.get('units')
        grade = request.POST.get('grade')
        marks = request.POST.get('marks')
        cgpa = request.POST.get('cgpa')

        Grade.objects.create(
            student=student,
            year=year,
            semester=semester,
            code=code,
            course=course,
            units=units,
            grade=grade,
            marks=marks,
            cgpa=cgpa
        )
        # --- ADDED SUCCESS MESSAGE ---
        messages.success(request, f"Grade for {course} added successfully!")
        return redirect('manage_grades')

    
    all_students = Student.objects.all()
    all_grades = Grade.objects.all().order_by('student__user__username', 'year', 'semester')

    context = {
        'students': all_students,
        'grades': all_grades,
    }
    return render(request, 'manage_grades.html', context)


# --- THIS IS THE NEW FUNCTION FOR EDITING GRADES ---
# It corresponds to the 'edit_grade' URL we created in Step 1

@login_required
def edit_grade_view(request, grade_id):
    """
    Handles editing a specific, existing grade.
    Only accessible by staff users.
    """
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('dashboard')

    # Get the specific grade from the database, or show a 404 error
    grade = get_object_or_404(Grade, id=grade_id)

    if request.method == 'POST':
        # Form was submitted, so save the new data
        student_id = request.POST.get('student')
        
        try:
            grade.student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            messages.error(request, "The selected student does not exist.")
            # Re-render the edit page with the error
            all_students = Student.objects.all()
            context = { 'grade': grade, 'students': all_students }
            return render(request, 'edit_grade.html', context)
            
        grade.year = request.POST.get('year')
        grade.semester = request.POST.get('semester')
        grade.code = request.POST.get('code')
        grade.course = request.POST.get('course')
        grade.units = request.POST.get('units')
        grade.grade = request.POST.get('grade')
        grade.marks = request.POST.get('marks')
        grade.cgpa = request.POST.get('cgpa')
        grade.save() # Save the changes to the existing grade
        
        messages.success(request, "Grade updated successfully!")
        return redirect('manage_grades') # Redirect back to the main list

    else:
        # Show the form pre-filled with the existing grade's data
        all_students = Student.objects.all()
        context = {
            'grade': grade,
            'students': all_students
        }
        # We will create this 'edit_grade.html' file in the next step
        return render(request, 'edit_grade.html', context)


# --- THIS IS THE NEW FUNCTION FOR DELETING GRADES ---
# It corresponds to the 'delete_grade' URL we created in Step 1

# --- THIS IS THE NEW FUNCTION FOR DELETING GRADES ---
@login_required
def delete_grade_view(request, grade_id):
    """
    Handles deleting a specific grade.
    Only accessible by staff users.
    """
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('dashboard')

    grade = get_object_or_404(Grade, id=grade_id)
    grade.delete()
    
    messages.success(request, "Grade deleted successfully.")
    return redirect('manage_grades')