from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField() 
    price = models.IntegerField() 

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=200)  # ✅ must exist
    seats = models.CharField(max_length=50)
    total_amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)