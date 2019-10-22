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
from datetime import datetime

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
}

movie = {
    'movieName':'',
    'duration':'',
    'movieRating':'',
    'director':'',
    'actor':'',
    'genre':''
}

movieSchedule = {
    'movie': movie,
    'totalSeat':'',
    'availableSeat':'',
    'theater': theater,
    'movieScheduleFlag':movieScheduleFlag,
    'room':'',
    'startTime':'',
    'endTime':''
}


def SearchTheaterWithPos(request):
    movieJson = ""
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
    except:
        longitude = 0.0
        latitude = 0.0
    
    print('long:{}, lat:{}'.format(latitude, longitude))

    # 현재는 메가박스에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        print("Dist {}".format(dist))
        if dist < 0.001:
            movie_list = MegaBoxCrawl(reqtheater, reqtheater.regionCode, reqtheater.theaterCode)
            for movie_Info in movie_list:
                
                movie_info = json.loads(movie_Info)

                movie['movieName'] = movie_info['movieName']
                movieObj = Movies.objects.get(movieName=movie_info["movieName"])
                movie['movieRating'] = movieObj.movieRating
                movie['duration'] = movieObj.movieRating
                movie['director'] = movieObj.movieRating
                movie['actor'] = movieObj.actor
                movie['genre'] = movieObj.genre


                theater['theaterName'] = reqtheater.theaterName
                theater['theaterCode'] = reqtheater.theaterCode
                theater['regionCode'] = reqtheater.regionCode
                theater['brand'] = reqtheater.brand

                movieSchedule['room'] = movie_info['room']
                movieSchedule['totalSeat'] = movie_info['totalSeat']
                movieSchedule['availableSeat'] = movie_info['avaliableSeat']
                movieSchedule['movie'] = movie
                movieSchedule['theater'] = theater
                movieSchedule['startTime'] = movie_info['startTime']
                movieSchedule['endTime'] = movie_info['endTime']

                movieJson += json.dumps(movieSchedule, ensure_ascii=False)

    return JsonResponse(movieJson, safe=False)



def SearchMovieListWithPos(request):
    try:
        theaterName = request.GET['theaterName']
    except:
        theaterName = "조커"
    reqTheater = Theaters.objects.get(theaterName=theaterName)
    # reqMovies = MovieSchedules.objects.filter(theater=reqTheater.id)
    
    movieinfo = MegaBoxCrawl(reqTheater, reqTheater.regionCode, reqTheater.theaterCode)
    return JsonResponse(movieinfo, safe=False)

def SearchMovieWithPos(request):
    moiveJson = dict()
    
    return JsonResponse(moiveJson)
# Create your views here.


def Test(request):
    testTheater = Theaters.objects.get(id=1)
    testTheater.updatedTime = datetime.now()
    testTheater.save()
    print(datetime.now())
    #GetMovieInfo("조커")
    return JsonResponse({
        'message':'안녕 파이썬 장고',
        'items' : ['python', 'django']
    })

'''
수정해야 할 것:
1) 영화스케쥴 정보 받아올때 Time 구조체로 영화 정보를 저장하자.
(즉, StartTime, endTime을 Time구조체로 수정)

2) json으로 보낼때 time구조체를 string으로 바꾸어서 보내줘야 한다. 
(즉, string type을 time type으로 time type을 string type으로 바꾸기 )

시도해 볼것:
dict에다가 time객체(또는 datetime객체)를 넣고 json으로 변환하면 어떻게 나올지 
확인해보자.


'''

'''

현재 시간 datetime으로 가져오기
import datetime
s = datetime.datetime.now()
2019-05-15 15:35:00.15464454

시간 끼리 빼기 연산이 가능하다!!
업데이트 한 시간과 비교했을 때 얼마나 지났는지 확인하고
업데이트된 시간이랑 15분 이상 차이나면 그 때 초기화하면 된다. 

그냥 비교하는 걸 함수로 만들어주자. 그리고 뺸 시간이을 데이, 날짜, 시간 분 등으로
파싱한다음에 분으로 묶어주고 비교하면 가능함

==> DateTime을 string값으로 바꿔야 한다. 
그래야 json에 넣을 때 이쁘게 넣을 수 있다. 


'''