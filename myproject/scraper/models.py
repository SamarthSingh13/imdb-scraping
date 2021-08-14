from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=2000)
    rating = models.FloatField(default=0.0)
    thumbnail_url = models.TextField()

