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
from .crawling import LotteCinemaCrawl
from .crawling import CGVCrawl
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
            'startTime':'{}:{}'.format(int(movieSchedule.startTime/100), movieSchedule.startTime%100),
            'endTime': '{}:{}'.format(int(movieSchedule.endTime/100), movieSchedule.endTime%100),
            'subtitle':movieSchedule.subtitle,
            'dubbing':movieSchedule.dubbing,
            'room property':"2D"
        }
        movieScheduleList.append(movieScheduleDict)
    return movieScheduleList

def GetMovie(movieID):
    movie = Movies.objects.get(id=movieID)
    movieEle = {
        'movieName':movie.movieName,
        'duration':movie.duration,
        'director':movie.director,
        'actors':movie.actors,
        'movieRating':movie.movieRating,
        'userRating':movie.userRating,
        'genre':movie.genre,
        'imgUrl':movie.imgUrl,
        'nation':movie.nation
    }
    return movieEle

def GetTheaterInfo(reqtheater, distance):
    theaterEle = {
        'theaterName':reqtheater.theaterName,
        'theaterCode':reqtheater.theaterCode,
        'regionCode':reqtheater.regionCode,
        'longitude':reqtheater.longitude,
        'latitude':reqtheater.latitude,
        'brand':reqtheater.brand,
        'distance':distance
    }
    return theaterEle

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

    # 현재는 메가박스 + 롯데시네마 에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='lottecinema'))
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
            diffTime = GetDiffTime(reqtheater.updatedTime, datetime.now())    
            if (diffTime > 60*15):
                if reqtheater.brand == 'megabox':
                    MegaBoxCrawl(reqtheater)
                elif reqtheater.brand == 'lottecinema':
                    LotteCinemaCrawl(reqtheater)

                reqtheater.updatedTime = datetime.now()
                reqtheater.save() 
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

def SearchLottecinemaMovie(request):
    allTheater = Theaters.objects.filter(brand__exact='lottecinema')
    movieJson = []
    for idx, reqtheater in enumerate(allTheater):
        movieList = LotteCinemaCrawl(reqtheater)
        movieJson.append(movieList)

    movieJson = json.dumps(movieJson, ensure_ascii=False)
    return HttpResponse(movieJson, content_type="text/json-comment-filtered")

def SearchCGVMovie(request):
    allTheater = Theaters.objects.filter(brand__exact='cgv')
    movieJson = []
    for idx, reqtheater in enumerate(allTheater):
        movieList = CGVCrawl(reqtheater)
        movieJson.append(movieList)
        if idx > 1:
            break

    movieJson = json.dumps(movieJson, ensure_ascii=False)
    return HttpResponse(movieJson, content_type="text/json-comment-filtered")

def SearchTheaterWithPos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
    except:
        longitude = 0.0
        latitude = 0.0
    

    # 현재는 메가박스 + 롯데시네마 에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.filter(brand__exact='lottecinema')
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='megabox'))

    theaterDistanceDict = dict()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 
    orderCnt = 0
    theater = []
    for theaterOrder in theaterOrderedSchedule:
        if orderCnt <= 20:
            orderCnt = orderCnt + 1
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            theaterEle = GetTheaterInfo(reqtheater, theaterOrder[1])
            theater.append(theaterEle)
        else:
            break
    movieJson = json.dumps(theater, ensure_ascii=False)

    return HttpResponse(movieJson, content_type="text/json-comment-filtered")



def SearchMovieListWithPos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
    except:
        longitude = 0.0
        latitude = 0.0
    
    # 현재는 메가박스 + 롯데시네마 에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='lottecinema'))

    theaterDistanceDict = dict()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 

    
    movieScheduleSet = None
    idx = 0
    for theaterOrder in theaterOrderedSchedule:
        if theaterOrder[1] <= 5000:
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            diffTime = GetDiffTime(reqtheater.updatedTime, datetime.now())    
            print(diffTime)
            if (diffTime > 60*15):
                if reqtheater.brand == 'megabox':
                    MegaBoxCrawl(reqtheater)
                elif reqtheater.brand == 'lottecinema':
                    LotteCinemaCrawl(reqtheater)

                reqtheater.updatedTime = datetime.now()
                reqtheater.save() 
            if idx == 0:
                movieScheduleSet = MovieSchedules.objects.filter(theater__exact=theaterOrder[0])
            else:
                movieScheduleSet = movieScheduleSet.union(MovieSchedules.objects.filter(theater__exact=theaterOrder[0]))
            idx = idx + 1
        else:
            break
    
    if movieScheduleSet == None:
        return None
    
    movieDict = dict()
    for movieSchedule in movieScheduleSet:
        movieID = movieSchedule.movie.id
        movieDict[movieID] = Movies.objects.get(id=movieID).userRating

    movie = []
    movieList = sorted(movieDict.items(),key=lambda x: x[1], reverse=True) 
   
    for movieOrder in movieList:
        movieEle = GetMovie(movieOrder[0])
        movie.append(movieEle)

    movieJson = json.dumps(movie, ensure_ascii=False)

    return HttpResponse(movieJson, content_type="text/json-comment-filtered")


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