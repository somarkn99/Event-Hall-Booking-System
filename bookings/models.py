from django.db import models
from accounts.models import User
from halls.models import Hall

class Booking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='bookings')
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        duration_in_hours = (self.end_datetime - self.start_datetime).total_seconds() / 3600
        self.total_price = self.hall.price_per_hour * duration_in_hours
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.full_name} - {self.hall.name} ({self.status})"
