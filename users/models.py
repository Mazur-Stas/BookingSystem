from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = [
        ("USER", "Користувач"),
        ("MANAGER", "Менеджер"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="users/avatars/", default="users/avatars/default.png", blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="USER")

    class Meta:
        ordering = ["user__username"]

    def __str__(self):
        return f"Профіль користувача {self.user.username}"