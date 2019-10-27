from django.db import models


class Movies(models.Model):
    objects = models.Manager()
    movieName = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    actors = models.CharField(max_length=50)
    movieRating = models.CharField(max_length=20)
    duration = models.IntegerField()
    genre = models.CharField(max_length=30)
    userRating = models.FloatField()
    imgUrl = models.CharField(max_length=50)
    nation = models.CharField(max_length=20)


    def __str__(self):
        return self.movieName

    class Meta:
        managed = True
        db_table = 'movies'


class Theaters(models.Model):
    objects = models.Manager()
    theaterName = models.CharField(max_length=20)
    regionCode = models.CharField(max_length=10)
    theaterCode = models.CharField(max_length=10)
    longitude = models.FloatField()
    latitude = models.FloatField()
    brand = models.CharField(max_length=30)
    updatedTime = models.DateTimeField()
    address = models.CharField(max_length=50)
    # >> theaterFlag
    # << theaterFlag

    def __str__(self):
        return self.brand + " " +  self.theaterName

    class Meta:
        managed = True
        db_table = 'theaters'

class MovieSchedules(models.Model):
    objects = models.Manager()
    movie = models.ForeignKey(Movies, related_name='MovieSchedules', on_delete=models.CASCADE)
    theater = models.ForeignKey(Theaters, models.DO_NOTHING)
    room = models.CharField(max_length=20)
    totalSeat = models.IntegerField()
    availableSeat = models.IntegerField()
    # movieCode = models.IntegerField(null=True, blank=True)
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    roomProperty = models.CharField(max_length=20)
    # >> movieScheduleFlag
    subtitle = models.BooleanField(null=True)
    dubbing = models.BooleanField(null=True)
    digitalized = models.BooleanField(null=True)
    lateNight = models.BooleanField(null=True)
    morning = models.BooleanField(null=True)
    # << movieScheduleFlag


    class Meta:
        managed = True
        db_table = 'movieschedules'
# Create your models here.
