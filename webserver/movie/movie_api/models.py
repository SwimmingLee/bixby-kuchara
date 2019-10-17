from django.db import models
from django.conf import settings

class Movie(models.Model):
    movieName = models.CharField(max_length=100)
    movieRoom = models.CharField(max_length=20)

    def __str__(self):
        return self.moiveName

    
# Create your models here.
