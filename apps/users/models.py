
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'Oddiy Foydalanuvchi'
        MANAGER = 'manager', 'Menejer'

    role = models.CharField(max_length=20,choices=RoleChoices.choices,default=RoleChoices.USER)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - ({self.get_role_display()})"