from django.contrib.auth.hashers import make_password
from auth.models import User

def set_passwords():
    # Retrieve all user objects
    users = User.objects.all()

    # Set password for each user to '123456'
    for user in users:
        user.set_password('123456')
        user.save()

if __name__ == "__main__":
    set_passwords()
