from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'
'''
class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		filed = ('id', 'title', 'genre', 'year')
'''