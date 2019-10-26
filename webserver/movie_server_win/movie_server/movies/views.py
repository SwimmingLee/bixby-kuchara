from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers

from .serializers import *
from .models import Movies
from .models import Theaters
from .models import MovieSchedules


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theaters.objects.all()
    serializer_class = TheaterSerializer

class MovieScheduleViewSet(viewsets.ModelViewSet):
    queryset = MovieSchedules.objects.all()
    serializer_class = MovieSchuduleSerializer

