from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Room(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="rooms/", blank=True, null=True)
    floor = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ("NEW", "Нова заявка"),
        ("APPROVED", "Підтверджено"),
        ("REJECTED", "Відхилено"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")

    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    purpose = models.CharField(max_length=255)

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="NEW")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.room.name} ({self.booking_date})"