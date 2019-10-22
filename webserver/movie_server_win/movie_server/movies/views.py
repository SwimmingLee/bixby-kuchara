from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse

from .serializers import MovieSchuduleSerializer
from .serializers import TheaterSerializer
from .serializers import MovieSerializer
from .serializers import NamedPointStructresSerializer

from .models import MovieSchedules
from .models import Movies
from .models import Theaters
from .models import NamedPointStructres

from .update import GetMovieInfo
from .update import GetNaverMovieInfo
from .crawling import MegaBoxCrawl
from .getdistance import get_euclidean_distance

import json


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theaters.objects.all()
    serializer_class = TheaterSerializer

class MovieScheduleViewSet(viewsets.ModelViewSet):
    queryset = MovieSchedules.objects.all()
    serializer_class = MovieSchuduleSerializer

class NamedPointStructureViewSet(viewsets.ModelViewSet):
    queryset = NamedPointStructres.objects.all()
    serializer_class = NamedPointStructresSerializer


theaterFlag = {
    'name':'경희대',
    'point': {
        'latitude':12.124,
        'longitude':32.154
    }
}

movieScheduleFlag = {
    'subtitle': True,        
    'dubbing': False,               
    'digitalized': True,           
    'lateNight': False,   
    'morning': False,
}

theater = {
    'theaterName': '',
    'theaterCode':'',
    'regionCode':'',
    'brand':'',
    'theaterFlag': theaterFlag
}

movie = {
    'movieName':'',
    'duration':'',
    'movieRating':'',
    'director':'',
    'actors':'',
    'genre':''
}

movieSchedule = {
    'movie': movie,
    'totalSeat':'',
    'availableSeat':'',
    'theater': theater,
    'movieScheduleFlag':movieScheduleFlag,
    'room':'',
}


def SearchTheaterWithPos(request):
    movieJson = ""
    try:
        longitude = float(request.GET['longitude'])
    except:
        longitude = 0.0
    
    try:
        latitude = float(request.GET['latitude'])
    except:
        latitude = 0.0

    print('long:{}, lat:{}'.format(latitude, longitude))

    # 현재는 메가박스에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        print("Dist {}".format(dist))
        if dist < 0.001:
            movie_list = MegaBoxCrawl(reqtheater.regionCode, reqtheater.theaterCode)
            for movie_Info in movie_list:
                
                movie_info = json.loads(movie_Info)

                movie['movieName'] = movie_info['movieName']
                movie['movieRating'] = movie_info['movieRating']

                theater['theaterName'] = reqtheater.theaterName
                theater['theaterCode'] = reqtheater.theaterCode
                theater['regionCode'] = reqtheater.regionCode
                theater['brand'] = reqtheater.brand

                movieSchedule['room'] = movie_info['room']
                movieSchedule['totalSeat'] = movie_info['seatInfo']
                movieSchedule['availableSeat'] = movie_info['seatInfo']
                movieSchedule['movie'] = movie
                movieSchedule['theater'] = theater

                movieJson += json.dumps(movieSchedule, ensure_ascii=False)

    return JsonResponse(movieJson, safe=False)



def SearchMovieListWithPos(request):
    try:
        theaterName = request.GET['theaterName']
    except:
        theaterName = "조커"
    reqTheater = Theaters.objects.get(theaterName=theaterName)
    # reqMovies = MovieSchedules.objects.filter(theater=reqTheater.id)
    
    movieinfo = MegaBoxCrawl(reqTheater.regionCode, reqTheater.theaterCode)
    return JsonResponse(movieinfo, safe=False)

def SearchMovieWithPos(request):
    moiveJson = dict()
    
    return JsonResponse(moiveJson)
# Create your views here.


def Test(request):
    GetMovieInfo("조커")
    return JsonResponse({
        'message':'안녕 파이썬 장고',
        'items' : ['python', 'django']
    })
