from rest_framework import serializers
from .models import MovieSchedules
from .models import Movies
from .models import Theaters
from .models import NamedPointStructres


# Theaters
# MovieSchedules
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theaters
        fields = '__all__'

class NamedPointStructresSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamedPointStructres
        fields= '__all__'


class MovieSchuduleSerializer(serializers.ModelSerializer):
    #print("Room_Test " +  room)
    #movie_images = MovieSerializer(read_only=True)
    #print("Hello")
    #print("HELLO :" + movie_images)
    #queryset = MovieSchedules.objects.all()
    #test = 10
   # theater_images = TheaterSerializer(many=True, read_only=True)
   # movie_images = serializers.RelatedField(source='Movie', many=True, read_only=True)
    #print(movie_images)
    class Meta:
        model = MovieSchedules
        fields = '__all__'