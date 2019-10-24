from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from django.core import serializers

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
from .jsonmodels import TheaterOrderedSchedule

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


def GetMovieScheduleList(reqtheater, movieID):
    diffTime = GetDiffTime(reqtheater.updatedTime, datetime.now())    
    if (diffTime > 60*15):
        MegaBoxCrawl(reqtheater)
        reqtheater.updatedTime = datetime.now()
        reqtheater.save() 

    movieScheduleList = []
    movieSchedules = MovieSchedules.objects.filter(theater__exact=reqtheater.id, movie__exact=movieID)
    for movieSchedule in movieSchedules:
        movieScheduleDict = {
            'room':movieSchedule.room,
            'totalSeat':movieSchedule.totalSeat,
            'availableSeat':movieSchedule.availableSeat,
            'startTime':movieSchedule.startTime,
            'endTime':movieSchedule.endTime,
            'subtitle':movieSchedule.subtitle,
            'dubbing':movieSchedule.dubbing,
            'room property':"2D"
        }
        movieScheduleList.append(movieScheduleDict)
    return movieScheduleList


def GetMovieScheduleDict(movie_info):
    movieScheduleDict = dict()
    movieScheduleDict['room'] = movie_info['room']
    movieScheduleDict['totalSeat'] = movie_info['totalSeat']
    movieScheduleDict['availableSeat'] = movie_info['avaliableSeat']
    movieScheduleDict['startTime'] = movie_info['startTime']
    movieScheduleDict['endTime'] = movie_info['endTime']
    movieScheduleDict['subtitle'] = False
    movieScheduleDict['dubbing'] = False
    movieScheduleDict['room property'] = "NoT IMAX"
    return movieScheduleDict

def GetDiffTime(preTime, curTime):
    curTime = curTime.replace(tzinfo=None)
    preTime = preTime.replace(tzinfo=None)
    diffTime = curTime - preTime
    #print(curTime)
    #print(preTime)
    #print(diffTime)
    return diffTime.total_seconds()


def SearchTheaterOrderedScheduleWithPos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
        movieName = request.GET['movieName']
    except:
        longitude = 0.0
        latitude = 0.0
    
    print('long:{}, lat:{}, movieName:{}'.format(latitude, longitude, movieName))

    # 현재는 메가박스에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    movieObj = Movies.objects.get(movieName=movieName)

    
    theaterDistanceDict = dict()
   
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 
    theater = []
    orderCnt = 0
    for theaterOrder in theaterOrderedSchedule:
        if orderCnt == 0 or theaterOrder[1] < 3000:
            orderCnt = orderCnt + 1
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            movieScheduleList = GetMovieScheduleList(reqtheater, movieObj.id)
            theaterEle = {
                'theaterInfo':reqtheater,
                'distance':theaterOrder[1],
                'theaterSchedule':movieScheduleList
            }
            theater.append(theaterEle)
        else:
            break

    TOS = TheaterOrderedSchedule(
        movie=movieObj,
        theater=theater
    )
    TOSdict = TOS.GetJson()
    movieJson = json.dumps(TOSdict, ensure_ascii=False)

    return HttpResponse(movieJson, content_type="text/json-comment-filtered")

def SearchMegaboxMovie(request):
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    for reqtheater in allTheater:
        MegaBoxCrawl(reqtheater)

    movieJson = {
        "megabox searching":"success"
    }
    movieJson = json.dumps(movieJson, ensure_ascii=False)
    return HttpResponse(movieJson, content_type="text/json-comment-filtered")

def SearchTheaterWithPos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
        movieName = request.GET['movieName']
    except:
        longitude = 0.0
        latitude = 0.0
    
    print('long:{}, lat:{}, movieName:{}'.format(latitude, longitude, movieName))

    # 현재는 메가박스에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    
    movieObj = Movies.objects.get(movieName=movieName)
    theater = []
    
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        print("Dist {}".format(dist))
        if dist < 0.05:
            movie_list = MegaBoxCrawl(reqtheater)
            timeScheduleList = []

            for movie_Info in movie_list:
                movie_info = json.loads(movie_Info)

                if movieName != movie_info['movieName']:
                    continue 

                movieScheduleDict = GetMovieScheduleDict(movie_info)
                timeScheduleList.append(movieScheduleDict)

            theaterEle = {
                'theaterInfo':reqtheater,
                'theaterSchedule':timeScheduleList
            }
            theater.append(theaterEle)

    TOS = TheaterOrderedSchedule(
        movie=movieObj,
        theater=theater
    )
    TOSdict = TOS.GetJson()
    movieJson = json.dumps(TOSdict, ensure_ascii=False)

    return HttpResponse(movieJson, content_type="text/json-comment-filtered")


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