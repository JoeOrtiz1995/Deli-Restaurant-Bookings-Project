from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.title}, starting {self.start_date}"