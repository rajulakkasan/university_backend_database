from django.contrib.auth.backends import BaseBackend
from .models import User

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username= username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
