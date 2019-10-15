from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSchuduleSerializer
from .models import MovieSchedules
from .models import Movies
from .models import Theaters

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieSchedules.objects.all()
    serializer_class = MovieSchuduleSerializer
    
# Create your views here.
