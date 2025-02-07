from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now, editable=False)  # Stores submission time

    def __str__(self):
        return f"{self.name} - {self.email}"
