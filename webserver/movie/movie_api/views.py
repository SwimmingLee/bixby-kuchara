from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

class MovieList(generics.ListCreateAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
