from django.db import models


class Movies(models.Model):
    movieName = models.CharField(max_length=20)
    movieDirector = models.CharField(max_length=20)
    # movieActor = models.????
    movieRating = models.CharField(max_length=20)
    movieRunningTime = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.movieName

    class Meta:
        managed = True
        db_table = 'movies'

class Theaters(models.Model):
    theaterName = models.CharField(max_length=20)
    region = models.IntegerField()
    spot = models.IntegerField()
    pos = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'theaters'

class MovieSchedules(models.Model):
    Movie = models.ForeignKey(Movies, related_name='MovieSchedules', on_delete=models.CASCADE)
    Theater = models.ForeignKey(Theaters, models.DO_NOTHING)
    room = models.CharField(max_length=20)
    startTime = models.CharField(max_length=10)
    endTime = models.CharField(max_length=10)

    def __str__(self):
        return self.Movie

    class Meta:
        managed = True
        db_table = 'movieschedules'
# Create your models here.
