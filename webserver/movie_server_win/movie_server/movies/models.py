from django.db import models


class Movies(models.Model):
    movieName = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    actor = models.CharField(max_length=50)
    movieRating = models.CharField(max_length=20)
    duration = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=30)
    userRating = models.FloatField()
    imgUrl = models.CharField(max_length=50)
    nation = models.CharField(max_length=20)

    def __str__(self):
        return self.movieName

    class Meta:
        managed = True
        db_table = 'movies'

class NamedPointStructres(models.Model):
    name = models.CharField(max_length=20)
    # >> point
    latitude = models.FloatField()
    longitude = models.FloatField()
    # << point


class Theaters(models.Model):
    theaterName = models.CharField(max_length=20)
    regionCode = models.IntegerField()
    theaterCode = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    brand = models.CharField(max_length=30)
    # >> theaterFlag
    # << theaterFlag

    class Meta:
        managed = True
        db_table = 'theaters'

class MovieSchedules(models.Model):
    movie = models.ForeignKey(Movies, related_name='MovieSchedules', on_delete=models.CASCADE)
    theater = models.ForeignKey(Theaters, models.DO_NOTHING)
    room = models.CharField(max_length=20)
    totalSeat = models.IntegerField()
    availableSeat = models.IntegerField()
    movieCode = models.IntegerField()
    startTime = models.CharField(max_length=10)
    endTime = models.CharField(max_length=10)
    # >> movieScheduleFlag
    subtitile = models.BooleanField()
    dubbing = models.BooleanField()
    digitalized = models.BooleanField()
    lateNight = models.BooleanField()
    morning = models.BooleanField()
    # << movieScheduleFlag


    def __str__(self):
        return self.movie.movieName

    class Meta:
        managed = True
        db_table = 'movieschedules'
# Create your models here.
