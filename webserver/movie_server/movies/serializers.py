from rest_framework import serializers
from .models import MovieSchedules
from .models import Movies
from .models import Theaters

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

class MovieSchuduleSerializer(serializers.ModelSerializer):
    movie_images = MovieSerializer(read_only=True)
   # theater_images = TheaterSerializer(many=True, read_only=True)
   # movie_images = serializers.RelatedField(source='Movie', many=True, read_only=True)
    #print(movie_images)
    class Meta:
        model = MovieSchedules
        fields = '__all__'