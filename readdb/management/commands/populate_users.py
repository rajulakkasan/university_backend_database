from django.core.management.base import BaseCommand
from readdb.models import Student, Instructor, User

class Command(BaseCommand):
    help = 'Populate user data from student and instructor models'

    def handle(self, *args, **kwargs):
        self.create_student_users()
        self.create_instructor_users()
        self.create_admin_user()

    def create_student_users(self):
        try:
            students = Student.objects.all()
            for student in students:
                username = f"{student.name.lower().replace(' ', '_')}_{student.id}"
                user = User.objects.create_user(
                    username=username,
                    password='123456',
                    user_type='student',
                    first_name=student.name,
                    is_superuser=False,
                    is_staff=False,
                    email='' 
                )
                self.stdout.write(self.style.SUCCESS(f"Created student user: {username}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error creating student user: {e}"))

    def create_instructor_users(self):
        try:
            instructors = Instructor.objects.all()
            for instructor in instructors:
                username = f"{instructor.name.lower().replace(' ', '_')}_{instructor.id}"
                user = User.objects.create_user(
                    username=username,
                    password='123456',
                    user_type='professor',
                    first_name=instructor.name,
                    is_superuser=False,
                    is_staff=True,
                    email='' 
                )
                self.stdout.write(self.style.SUCCESS(f"Created instructor user: {username}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error creating instructor user: {e}"))

    def create_admin_user(self):
        try:
            admin_user = User.objects.create_user(
                username='admin',
                password='123456',
                user_type='admin',
                first_name='Admin',
                is_superuser=True,
                is_staff=True,
                email='' 
            )
            self.stdout.write(self.style.SUCCESS("Created admin user: admin"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error creating admin user: {e}"))
