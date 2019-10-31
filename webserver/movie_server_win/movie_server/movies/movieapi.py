from django.http import JsonResponse, HttpResponse
import json
from .crawling import MovieCrawl
from .crawling_multi import taskQueue
from .getdistance import get_euclidean_distance
from .models import Movies
from .models import Theaters
from .models import MovieSchedules
from .jsonmodels import GetMovieScheduleList
from .jsonmodels import GetTheaterInfo2ByObj
from .jsonmodels import GetTheaterInfoByObj
from .jsonmodels import GetMovieScheduleInfoByObj
from .jsonmodels import GetMovieInfoByID
from .jsonmodels import GetMovieInfoByObj
from .jsonmodels import TheaterOrderedSchedule
from multiprocessing import Process, Queue
import copy
import sys



def SearchTimeOrderedScheduleWithPos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
    except:
        return HttpResponse("{'invalid data': 'error'}", content_type="text/json-comment-filtered")
    
    allTheater = Theaters.objects.all()

    theaterDistanceDict = dict()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    DistanceOrderedTheater = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 

    movieScheduleSet = None
    nearTheaterlist = []
    processes = []
    for orderCnt, theaterOrder in enumerate(DistanceOrderedTheater):
        if orderCnt < 2 or theaterOrder[1] <= 5000:
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            MovieCrawl(reqtheater)
            nearTheaterlist.append(theaterOrder[0])
        else:
            break

    movieScheduleSet = MovieSchedules.objects.filter(theater__in=nearTheaterlist)
    movieScheduleSet = movieScheduleSet.order_by('startTime')

    MovieTheaterScheduleList = []
    for movieSchedule in movieScheduleSet:
        MovieTheaterSchedule = {
            'movie':GetMovieInfoByObj(movieSchedule.movie),
            'theaterInfo':GetTheaterInfo2ByObj(movieSchedule.theater, theaterDistanceDict[movieSchedule.theater.id]),
            'theaterSchedule': GetMovieScheduleInfoByObj(movieSchedule)
        }
        MovieTheaterScheduleList.append(copy.copy(MovieTheaterSchedule))
    movieJson = json.dumps(MovieTheaterScheduleList, ensure_ascii=False)

    return HttpResponse(movieJson, content_type="text/json-comment-filtered")


def SearchTheaterOrderedScheduleWithPos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
        movieName = request.GET['movieName']
    except: 
        longitude = 0.0
        latitude = 0.0
    
    print('long:{}, lat:{}, movieName:{}'.format(latitude, longitude, movieName))
    sys.stdout.flush()

    # 현재는 메가박스 + 롯데시네마 에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.all()
       
    theaterDistanceDict = dict()
   
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 
    theater = []

    searchCnt = 0
    processes = []
    for orderCnt, theaterOrder in enumerate(theaterOrderedSchedule):
        if theaterOrder[1] <= 5000 or (searchCnt < 2 and orderCnt < 5):
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            MovieCrawl(reqtheater)
            movieObj = Movies.objects.filter(movieName__exact=movieName)
            if movieObj.count() == 0:
                continue
            movieObj = movieObj.first()
    
            movieScheduleList = GetMovieScheduleList(reqtheater, movieObj.id)
            theaterEle = {
                'theaterInfo':reqtheater,
                'distance':theaterOrder[1],
                'theaterSchedule':movieScheduleList
            }
            if len(movieScheduleList) > 0:
                searchrCnt = searchCnt + 1
                theater.append(theaterEle)
        else:
            break

    if len(theater) == 0:
        return HttpResponse("{'no search cinema schedule': 'error'}", content_type="text/json-comment-filtered")

    TOS = TheaterOrderedSchedule(
        movie=movieObj,
        theater=theater
    )
    TOSdict = TOS.GetJson()
    movieJson = json.dumps(TOSdict, ensure_ascii=False)


    return HttpResponse(movieJson, content_type="text/json-comment-filtered")


def SearchTheaterWithMoviePos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
        movieName = request.GET['movieName']
    except:
        return HttpResponse("{'invalid data': 'error'}", content_type="text/json-comment-filtered")
        # 현재는 메가박스 + 롯데시네마 에 대한 정보만 가져올 수 있도록 되어 있다. 
   
    allTheater = Theaters.objects.all()

    theaterDistanceDict = dict()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 
    
    theater = []
    movieObj = Movies.objects.get(movieName=movieName)

    for orderCnt, theaterOrder in enumerate(theaterOrderedSchedule):
        if orderCnt < 15:
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            
            if len(MovieSchedules.objects.filter(theater__exact=theaterOrder[0], movie__exact=movieObj.id)) > 0:
                theaterEle = GetTheaterInfo2ByObj(reqtheater, theaterOrder[1])
                theaterEle.update({'address':reqtheater.address})
                theater.append(theaterEle)
        else:
            break
    movieJson = json.dumps(theater, ensure_ascii=False)
    return HttpResponse(movieJson, content_type="text/json-comment-filtered")


def SearchTheaterWithPos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
    except:
        longitude = 0.0
        latitude = 0.0
    

    # 현재는 메가박스 + 롯데시네마 에 대한 정보만 가져올 수 있도록 되어 있다. 
    allTheater = Theaters.objects.all()

    theaterDistanceDict = dict()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 
    
    theater = []
    for orderCnt, theaterOrder in enumerate(theaterOrderedSchedule):
        if orderCnt < 15:
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            theaterEle = GetTheaterInfo2ByObj(reqtheater, theaterOrder[1])
            theaterEle.update({'address':reqtheater.address})
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
    allTheater = Theaters.objects.all()

    theaterDistanceDict = dict()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 
    
    movieScheduleSet = None
    nearTheaterlist = []
    processes = []
    for orderCnt, theaterOrder in enumerate(theaterOrderedSchedule):
        if orderCnt < 2 or theaterOrder[1] <= 5000:
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            MovieCrawl(reqtheater)
            #processes.append(Process(target=MovieCrawl, args=(reqtheater, taskQueue, )))
            nearTheaterlist.append(theaterOrder[0])
        else:
            break

    movieScheduleSet = MovieSchedules.objects.filter(theater__in=nearTheaterlist)
    if movieScheduleSet == None:
        return HttpResponse("{'no search cinema': 'error'}", content_type="text/json-comment-filtered")
    
    movieDict = dict()

    for movieSchedule in movieScheduleSet:
        movieID = movieSchedule.movie.id
        movieDict[movieID] = Movies.objects.get(id=movieID).userRating

    movie = []
    movieList = sorted(movieDict.items(),key=lambda x: x[1], reverse=True) 
   
    for movieOrder in movieList:
        movieEle = GetMovieInfoByID(movieOrder[0])
        movie.append(movieEle)

    movieJson = json.dumps(movie, ensure_ascii=False)

    return HttpResponse(movieJson, content_type="text/json-comment-filtered")



def SearchMovieScheduleWithMovieTheater(request):
    try:
        regionCode = request.GET['regionCode']
        theaterCode = request.GET['theaterCode']
        brand = request.GET['brand']
        movieName = request.GET['movieName']
    except:
        return HttpResponse({"invalid data":"transferred data is bad"}, content_type="text/json-comment-filtered")
    
    theaterObj = Theaters.objects.get(brand=brand, regionCode=regionCode, theaterCode=theaterCode)
    MovieCrawl(theaterObj)
    movieObj = Movies.objects.get(movieName=movieName)
    movieScheduleSet = MovieSchedules.objects.filter(theater__exact=theaterObj.id, movie=movieObj.id)

    MovieTheaterScheduleList = []
    for movieSchedule in movieScheduleSet:
        MovieTheaterSchedule = {
            'movie':GetMovieInfoByObj(movieObj),
            'theaterInfo':GetTheaterInfoByObj(theaterObj),
            'theaterSchedule': GetMovieScheduleInfoByObj(movieSchedule)
        }
        MovieTheaterScheduleList.append(copy.copy(MovieTheaterSchedule))
    movieJson = json.dumps(MovieTheaterScheduleList, ensure_ascii=False)

    return HttpResponse(movieJson, content_type="text/json-comment-filtered")


def SearchMovieScheduleWithTheater(request):
    i = 0
