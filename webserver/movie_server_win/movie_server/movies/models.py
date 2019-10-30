from django.db import models


class Movies(models.Model):
    objects = models.Manager()
    movieName = models.TextField()
    director = models.TextField()
    actors = models.TextField()
    movieRating = models.TextField()
    duration = models.IntegerField()
    genre = models.TextField()
    userRating = models.FloatField()
    imgUrl = models.TextField()
    nation = models.TextField()


    def __str__(self):
        return self.movieName

    class Meta:
        managed = True
        db_table = 'movies'


class Theaters(models.Model):
    objects = models.Manager()
    theaterName = models.TextField()
    regionCode = models.CharField(max_length=10)
    theaterCode = models.CharField(max_length=10)
    longitude = models.FloatField()
    latitude = models.FloatField()
    brand = models.CharField(max_length=30)
    updatedTime = models.DateTimeField()
    address = models.TextField()
    # >> theaterFlag
    # << theaterFlag

    def __str__(self):
        return self.brand + " " +  self.theaterName

    class Meta:
        managed = True
        db_table = 'theaters'

class MovieSchedules(models.Model):
    objects = models.Manager()
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    theater = models.ForeignKey(Theaters, models.DO_NOTHING)
    room = models.TextField()
    totalSeat = models.IntegerField()
    availableSeat = models.IntegerField()
    # movieCode = models.IntegerField(null=True, blank=True)
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    roomProperty = models.CharField(max_length=30)
    scheduleDate = models.IntegerField()
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
