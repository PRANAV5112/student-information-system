# students/migrations/0003_seed_default_grades_for_all_students.py

from django.db import migrations

# --- THIS IS THE DEFAULT GRADE LIST ---
GRADE_DATA = [
    # --- 2023-2024 / I ---
    {'year': '2023-2024', 'semester': 'I', 'code': 'CS101', 'course': 'Computer Programming', 'units': 4, 'grade': 'B', 'marks': '', 'cgpa': '6.3'},
    {'year': '2023-2024', 'semester': 'I', 'code': 'MT102', 'course': 'Engineering Graphics', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'I', 'code': 'EG101', 'course': 'English Language Skills', 'units': 3, 'grade': 'B+', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'I', 'code': 'CH102', 'course': 'Environmental Sciences', 'units': 2, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'I', 'code': 'HS101', 'course': 'Essence of Indian Traditional Knowledge', 'units': 0, 'grade': 'S', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'I', 'code': 'MA101', 'course': 'Linear Algebra and Ordinary Differential Equations', 'units': 3, 'grade': 'B+', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'I', 'code': 'PH101', 'course': 'Physics', 'units': 5, 'grade': 'B', 'marks': '13', 'cgpa': ''},
    
    # --- 2023-2024 / II ---
    {'year': '2023-2024', 'semester': 'II', 'code': 'EC101', 'course': 'Basic Electronics', 'units': 4, 'grade': 'B', 'marks': '', 'cgpa': '6.7'},
    {'year': '2023-2024', 'semester': 'II', 'code': 'CH101', 'course': 'Chemistry', 'units': 4, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'II', 'code': 'CS102', 'course': 'Data Structures', 'units': 4, 'grade': 'B+', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'II', 'code': 'MT101', 'course': 'Digital Fabrication', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'II', 'code': 'MA102', 'course': 'Higher Calculus', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'II', 'code': 'DS101', 'course': 'Introduction to AI and DS', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2023-2024', 'semester': 'II', 'code': 'EG102', 'course': 'Professional Communication', 'units': 3, 'grade': 'A', 'marks': '37', 'cgpa': ''},
    
    # --- 2024-2025 / III ---
    {'year': '2024-2025', 'semester': 'III', 'code': 'CS203', 'course': 'DESIGN AND ANALYSIS OF ALGORITHMS', 'units': 3, 'grade': 'A', 'marks': '', 'cgpa': '7.04'},
    {'year': '2024-2025', 'semester': 'III', 'code': 'MA202', 'course': 'DISCRETE MATHEMATICS', 'units': 3, 'grade': 'B+', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'III', 'code': 'MG201', 'course': 'ENGINEERING ECONOMICS AND MANAGEMENT', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'III', 'code': 'MA201', 'course': 'INTEGRAL TRANSFORMS AND PROBABILITY & STATISTICS', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'III', 'code': 'EC201', 'course': 'INTRODUCTION TO IOT', 'units': 3, 'grade': 'A+', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'III', 'code': 'CS201', 'course': 'OBJECT ORIENTED PROGRAMMING CONCEPTS', 'units': 4, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'III', 'code': 'CR201', 'course': 'POWER SKILLS-I', 'units': 1, 'grade': 'A+', 'marks': '57', 'cgpa': ''},
    
    # --- 2024-2025 / IV ---
    {'year': '2024-2025', 'semester': 'IV', 'code': 'CS202', 'course': 'THEORY OF COMPUTATION', 'units': 0, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'IV', 'code': 'CS204', 'course': 'COMPUTER ORGANIZATION AND ARCHITECTURE', 'units': 3, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'IV', 'code': 'DS203', 'course': 'DATA SCIENCE', 'units': 3, 'grade': 'B+', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'IV', 'code': 'CS206', 'course': 'DATABASE MANAGEMENT SYSTEMS', 'units': 0, 'grade': 'B+', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'IV', 'code': 'HS201', 'course': 'DYNAMICS OF SOCIAL CHANGE', 'units': 0, 'grade': 'B', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'IV', 'code': 'EC102', 'course': 'FUNDAMENTALS OF SIGNAL PROCESSING', 'units': 0, 'grade': 'A', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'IV', 'code': 'DS202', 'course': 'INDUSTRY CODING PRACTICE(PYTHON/R)', 'units': 3, 'grade': 'A', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'IV', 'code': 'CR202', 'course': 'POWER SKILLS - II', 'units': 1, 'grade': 'A+', 'marks': '', 'cgpa': ''},
    {'year': '2024-2025', 'semester': 'IV', 'code': 'CS205', 'course': 'WEB-ENABLED TECHNOLOGIES', 'units': 4, 'grade': 'A', 'marks': '74', 'cgpa': '6.5'},
]


def load_default_grades_for_all_students(apps, schema_editor):
    """
    This function finds EVERY student and gives them a copy of
    the GRADE_DATA list.
    """
    # We must get the models this way for a data migration
    Student = apps.get_model('students', 'Student')
    Grade = apps.get_model('students', 'Grade')
    
    # --- THIS IS THE NEW LOGIC ---
    # Instead of one student, we get ALL of them.
    all_students = Student.objects.all()

    if not all_students.exists():
        print("\nWARNING: No students found in the database to migrate.")
        return

    print(f"\nFound {all_students.count()} students. Adding default grade list to all...")

    # Loop 1: Iterate over every student in the database
    for student in all_students:
        print(f"  ... processing grades for {student.user.username}")
        
        # Loop 2: Iterate over the default grade list
        for entry in GRADE_DATA:
            # Use get_or_create to add the grade for THIS student
            # This also prevents duplicates if you ever run it again
            Grade.objects.update_or_create(
                student=student,  # This is the key change
                code=entry['code'],
                defaults={
                    'year': entry['year'],
                    'semester': entry['semester'],
                    'course': entry['course'],
                    'units': entry['units'],
                    'grade': entry['grade'],
                    'marks': entry['marks'],
                    'cgpa': entry['cgpa'],
                }
            )
    print("Default grade seeding complete for all students.")


class Migration(migrations.Migration):

    dependencies = [
        # This MUST point to your previous migration file
        ('students', '0002_alter_parent_students_grade'),
    ]

    operations = [
        # This line tells Django to run our custom function
        migrations.RunPython(load_default_grades_for_all_students),
    ]