import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Student


# Create and check models
def add_students():
    Student.objects.create(
        student_id = 'FC5204',
        first_name = 'John',
        last_name = 'Doe',
        birth_date = '1995-05-15',
        email = 'john.doe@university.com'
    )

    Student.objects.create(
        student_id = 'FE0054',
        first_name = 'Jane',
        last_name = 'Smith',
        birth_date = None,
        email = 'jane.smith@university.com'
    )
    
    student1 = Student(
        student_id = 'FH2014',
        first_name = 'Alice',
        last_name = 'Johnson',
        birth_date = '1998-02-10',
        email = 'alice.johnson@university.com'
    )
    student1.save()
    
    student2 = Student(
        student_id = 'FH2015',
        first_name = 'Bob',
        last_name = 'Wilson',
        birth_date = '1996-11-25',
        email = 'bob.wilson@university.com'
    )
    student2.save()


def get_students_info():
    students = Student.objects.all()
    students_info = []
    
    for student in students:
        students_info.append(f"Student №{student.student_id}: "
                             f"{student.first_name} {student.last_name}; "
                             f"Email: {student.email}")
    
    return '\n'.join(students_info)


def update_students_emails():
    students = Student.objects.all()
    
    for student in students:
        new_email = student.email.replace('university.com', 'uni-students.com')
        student.email = new_email
        student.save()


def truncate_students():
    students = Student.objects.all()
    students.delete()


# Run and print your queries
