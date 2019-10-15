from django.db import models
from django.conf import settings

class Booking(models.Model):
	subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='bookings')

	date_from = models.DateField()
	date_to = models.DateField(null=True, blank=True)
	room = models.CharField(max_length=100)
	note = models.TextField()

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.subscriber.username + " " + self.room
	

	class Meta:
		ordering = ['-date_from']

'''
class Movie(models.Model):
	title = models.CharField(max_length=30)
	genre = models.CharField(max_length=15)
	year = models.IntegerField()

	def __str__(self):
		return self.title
'''	
