from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="users/avatars/", default="users/avatars/default.png", blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    ROLE_CHOICES = [
        ("USER", "Користувач"),
        ("MANAGER", "Менеджер"),
        ("ADMIN", "Адміністратор"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="USER")

    def __str__(self):
        return f"Профіль {self.user.username}"