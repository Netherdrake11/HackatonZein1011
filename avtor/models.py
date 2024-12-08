from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta

class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    blocked_until = models.DateTimeField()

    def is_blocked(self):
        return self.blocked_until > timezone.now()

    def __str__(self):
        return f"IP {self.ip_address} заблокирован до {self.blocked_until}"


