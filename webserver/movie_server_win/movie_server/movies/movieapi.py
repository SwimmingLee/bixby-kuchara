from django.http import JsonResponse, HttpResponse
import json
from .crawling import MovieCrawl
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
import copy
import sys



def SearchTimeOrderedScheduleWithPos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
    except:
        return HttpResponse("{'invalid data': 'error'}", content_type="text/json-comment-filtered")
    
    allTheater = Theaters.objects.filter(brand__exact='cgv')
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='lottecinema'))
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='megabox'))

    theaterDistanceDict = dict()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    DistanceOrderedTheater = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 

    movieScheduleSet = None
    for orderCnt, theaterOrder in enumerate(DistanceOrderedTheater):
        if orderCnt == 0:
            movieScheduleSet = MovieSchedules.objects.filter(theater=theaterOrder[0])
        elif orderCnt <= 5:
            movieScheduleSet = movieScheduleSet.union(MovieSchedules.objects.filter(theater=theaterOrder[0]))
        else:
            break

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
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='cgv'))
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='lottecinema'))
       
    theaterDistanceDict = dict()
   
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 
    theater = []
    orderCnt = 0
    for theaterOrder in theaterOrderedSchedule:
        if orderCnt == 0 or theaterOrder[1] < 5000:
            orderCnt = orderCnt + 1
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            MovieCrawl(reqtheater)
            movieObj = Movies.objects.get(movieName=movieName)

            movieScheduleList = GetMovieScheduleList(reqtheater, movieObj.id)
            theaterEle = {
                'theaterInfo':reqtheater,
                'distance':theaterOrder[1],
                'theaterSchedule':movieScheduleList
            }
            if len(movieScheduleList) > 0:
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


def SearchTheaterWithMoviePos(request):
    try:
        longitude = float(request.GET['longitude'])
        latitude = float(request.GET['latitude'])
        movieName = request.GET['movieName']
    except:
        return HttpResponse("{'invalid data': 'error'}", content_type="text/json-comment-filtered")
        # 현재는 메가박스 + 롯데시네마 에 대한 정보만 가져올 수 있도록 되어 있다. 
   
    allTheater = Theaters.objects.filter(brand__exact='cgv')
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='lottecinema'))
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='megabox'))

    theaterDistanceDict = dict()
    for reqtheater in allTheater:
        dist = get_euclidean_distance(reqtheater.latitude, reqtheater.longitude, latitude, longitude)
        theaterDistanceDict[reqtheater.id] = dist

    theaterOrderedSchedule = sorted(theaterDistanceDict.items(),key=lambda x: x[1]) 
    
    theater = []
    movieObj = Movies.objects.get(movieName=movieName)

    for orderCnt, theaterOrder in enumerate(theaterOrderedSchedule):
        if orderCnt <= 10:
            reqtheater = Theaters.objects.get(id=theaterOrder[0])
            MovieCrawl(reqtheater)
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
    allTheater = Theaters.objects.filter(brand__exact='cgv')
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='lottecinema'))
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
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    allTheater = allTheater.union(Theaters.objects.filter(brand__exact='cgv'))
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
            MovieCrawl(reqtheater)

            if idx == 0:
                movieScheduleSet = MovieSchedules.objects.filter(theater__exact=theaterOrder[0])
            else:
                movieScheduleSet = movieScheduleSet.union(MovieSchedules.objects.filter(theater__exact=theaterOrder[0]))
            idx = idx + 1
        else:
            break
    
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
