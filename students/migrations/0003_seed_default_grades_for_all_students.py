# students/migrations/0003_seed_default_grades_for_all_students.py

from django.db import migrations
from django.contrib.auth.hashers import make_password

def populate_grades(apps, schema_editor):
    """
    Populates the database with default grades for a list of specific students.
    If the users do not exist, it CREATES them first.
    """
    User = apps.get_model('auth', 'User')
    Student = apps.get_model('students', 'Student')
    Grade = apps.get_model('students', 'Grade')

    # --- 1. DEFINE THE USERS YOU WANT TO SEED ---
    # Add any usernames you want here.
    usernames_to_seed = ['pranav', '23stuchh011079', '23stuchh0110193']

    # --- 2. DEFINE GRADES DATA ---
    grades_data = [
        # Semester I (2023-2024)
        {'year': '2023-2024', 'semester': 'I', 'code': 'CS101', 'course': 'Computer Programming', 'units': 4, 'grade': 'B', 'marks': '', 'cgpa': '6.3'},
        {'year': '2023-2024', 'semester': 'I', 'code': 'MT102', 'course': 'Engineering Graphics', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': '6.3'},
        {'year': '2023-2024', 'semester': 'I', 'code': 'EG101', 'course': 'English Language Skills', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': '6.3'},
        {'year': '2023-2024', 'semester': 'I', 'code': 'CH102', 'course': 'Environmental Sciences', 'units': 2, 'grade': 'B', 'marks': '', 'cgpa': '6.3'},
        {'year': '2023-2024', 'semester': 'I', 'code': 'HS101', 'course': 'Essence of Indian Traditional Knowledge', 'units': 0, 'grade': 'S', 'marks': '', 'cgpa': '6.3'},
        {'year': '2023-2024', 'semester': 'I', 'code': 'MA101', 'course': 'Linear Algebra and Ordinary Differential Equations', 'units': 3, 'grade': 'B+', 'marks': '', 'cgpa': '6.3'},

        # Semester II (2023-2024)
        {'year': '2023-2024', 'semester': 'II', 'code': 'PHY101', 'course': 'Physics', 'units': 5, 'grade': 'B', 'marks': '13', 'cgpa': '6.7'},
        {'year': '2023-2024', 'semester': 'II', 'code': 'EC101', 'course': 'Basic Electronics', 'units': 4, 'grade': 'B', 'marks': '', 'cgpa': '6.7'},
        {'year': '2023-2024', 'semester': 'II', 'code': 'CH101', 'course': 'Chemistry', 'units': 4, 'grade': 'B', 'marks': '', 'cgpa': '6.7'},
        {'year': '2023-2024', 'semester': 'II', 'code': 'CS102', 'course': 'Data Structures', 'units': 4, 'grade': 'B+', 'marks': '', 'cgpa': '6.7'},
        {'year': '2023-2024', 'semester': 'II', 'code': 'MT101', 'course': 'Digital Fabrication', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': '6.7'},
        {'year': '2023-2024', 'semester': 'II', 'code': 'MA102', 'course': 'Higher Calculus', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': '6.7'},
        {'year': '2023-2024', 'semester': 'II', 'code': 'DS101', 'course': 'Introduction to AI and DS', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': '6.7'},
        
        # Semester III (2024-2025)
        {'year': '2024-2025', 'semester': 'III', 'code': 'EG102', 'course': 'Professional Communication', 'units': 3, 'grade': 'A', 'marks': '37', 'cgpa': '7.04'},
        {'year': '2024-2025', 'semester': 'III', 'code': 'CS203', 'course': 'DESIGN AND ANALYSIS OF ALGORITHMS', 'units': 3, 'grade': 'A+', 'marks': '', 'cgpa': '7.04'},
        {'year': '2024-2025', 'semester': 'III', 'code': 'MA202', 'course': 'DISCRETE MATHEMATICS', 'units': 3, 'grade': 'B+', 'marks': '', 'cgpa': '7.04'},
        {'year': '2024-2025', 'semester': 'III', 'code': 'MG201', 'course': 'ENGINEERING ECONOMICS AND MANAGEMENT', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': '7.04'},
        {'year': '2024-2025', 'semester': 'III', 'code': 'MA201', 'course': 'INTEGRAL TRANSFORMS AND PROBABILITY & STATISTICS', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': '7.04'},
        {'year': '2024-2025', 'semester': 'III', 'code': 'EC201', 'course': 'INTRODUCTION TO IOT', 'units': 3, 'grade': 'A+', 'marks': '', 'cgpa': '7.04'},
        {'year': '2024-2025', 'semester': 'III', 'code': 'CS201', 'course': 'OBJECT ORIENTED PROGRAMMING CONCEPTS', 'units': 4, 'grade': 'B', 'marks': '', 'cgpa': '7.04'},

        # Semester IV (2024-2025)
        {'year': '2024-2025', 'semester': 'IV', 'code': 'CR001', 'course': 'POWER SKILLS-I', 'units': 1, 'grade': 'A+', 'marks': '57', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'CS202', 'course': 'THEORY OF COMPUTATION', 'units': 0, 'grade': 'B', 'marks': '', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'CS204', 'course': 'COMPUTER ORGANIZATION AND ARCHITECTURE', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'DS203', 'course': 'DATA SCIENCE', 'units': 3, 'grade': 'B+', 'marks': '', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'CS206', 'course': 'DATABASE MANAGEMENT SYSTEMS', 'units': 0, 'grade': 'B+', 'marks': '', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'HS201', 'course': 'DYNAMICS OF SOCIAL CHANGE', 'units': 3, 'grade': 'B+', 'marks': '', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'EC102', 'course': 'FUNDAMENTALS OF SIGNAL PROCESSING', 'units': 0, 'grade': 'A', 'marks': '', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'DS202', 'course': 'INDUSTRY CODING PRACTICE(PYTHON/R)', 'units': 3, 'grade': 'A', 'marks': '', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'CR202', 'course': 'POWER SKILLS - II', 'units': 1, 'grade': 'A+', 'marks': '', 'cgpa': '7.0'},
        {'year': '2024-2025', 'semester': 'IV', 'code': 'CS205', 'course': 'WEB-ENABLED TECHNOLOGIES', 'units': 4, 'grade': 'B', 'marks': '74', 'cgpa': '7.0'},
    ]

    # --- 3. LOOP THROUGH USERS AND ADD GRADES ---
    for username in usernames_to_seed:
        # Create or Get User
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': f'{username}@example.com',
                'password': make_password(',.Password@123'), # Default password
                'is_staff': False,
                'is_superuser': False
            }
        )

        # Create or Get Student Profile
        student_profile, created = Student.objects.get_or_create(user=user)

        # Add Grades for this Student using update_or_create
        for data in grades_data:
            Grade.objects.update_or_create(
                student=student_profile, 
                code=data['code'], 
                defaults=data
            )

class Migration(migrations.Migration):

    dependencies = [
        # MAKE SURE THIS MATCHES THE PREVIOUS MIGRATION FILE IN YOUR FOLDER
        ('students', '0002_alter_parent_students_grade'), 
    ]

    operations = [
        migrations.RunPython(populate_grades),
    ]