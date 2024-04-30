from readdb.models import Student, Instructor, User

# Function to create users from student data
def create_student_users():
    students = Student.objects.all()
    for student in students:
        # Create username using name and ID
        username = f"{student.name.lower().replace(' ', '_')}_{student.id}"
        # Create user
        print(username)
        user = User.objects.create_user(
            username=username,
            password='123456',
            user_type='student',
            first_name=student.name,
            email=''  # Set email if available
        )
        print(user)
        user.save()

# Function to create users from instructor data
def create_instructor_users():
    instructors = Instructor.objects.all()
    for instructor in instructors:
        # Create username using name and ID
        username = f"{instructor.name.lower().replace(' ', '_')}_{instructor.id}"
        # Create user
        print(username)
        user = User.objects.create_user(
            username=username,
            password='123456',
            user_type='professor',
            first_name=instructor.name,
            email=''  # Set email if available
        )
        print(user)
        user.save()

# Function to create admin user
def create_admin_user():
    # Create admin user
    admin_user = User.objects.create_user(
        username='admin',
        password='123456',
        user_type='admin',
        first_name='Admin',
        email=''  # Set email if available
    )
    admin_user.save()

# Main function to run the script
def main():
    create_student_users()
    create_instructor_users()
    create_admin_user()

if __name__ == "__main__":
    main()
