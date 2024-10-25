from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class BookingRequest(models.Model):
    full_name = models.CharField(max_length=100)
    date_request = models.DateField(auto_now_add=False)
    time_request = models.TimeField(auto_now_add=False)
    guests = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Booking Request from: {self.full_name}"