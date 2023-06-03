from django.db import models
from django.utils import timezone

class Contact(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
