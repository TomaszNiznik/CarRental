# users/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Możesz dodać dodatkowe pola, jeśli chcesz
    pass
