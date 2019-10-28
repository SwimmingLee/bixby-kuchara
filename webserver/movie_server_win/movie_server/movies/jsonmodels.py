import json
import datetime
from .models import Movies
from .models import Theaters
from .models import MovieSchedules

def GetDiffTime(preTime, curTime):
    curTime = curTime.replace(tzinfo=None)
    preTime = preTime.replace(tzinfo=None)
    diffTime = curTime - preTime
    return diffTime.total_seconds()

def GetMovieInfoByObj(movieObj):
    movieEle = {
        'movieName':movieObj.movieName,
        'duration':movieObj.duration,
        'director':movieObj.director,
        'actors':movieObj.actors,
        'movieRating':movieObj.movieRating,
        'userRating':movieObj.userRating,
        'genre':movieObj.genre,
        'imgUrl':movieObj.imgUrl,
        'nation':movieObj.nation
    }
    return movieEle

def GetMovieInfoByID(movieID):
    movieObj = Movies.objects.get(id=movieID)
    movieEle = GetMovieInfoByObj(movieObj)
    return movieEle

def GetTheaterInfoByObj(theaterObj):
    theaterInfoEle = {
        'theaterName':theaterObj.theaterName,
        'theaterCode':theaterObj.theaterCode,
        'regionCode':theaterObj.regionCode,
        'longitude':theaterObj.longitude,
        'latitude':theaterObj.latitude,
        'brand':theaterObj.brand,
    }
    return theaterInfoEle

def GetTheaterInfo2ByObj(theaterObj, distance):
    theaterInfoEle = GetTheaterInfoByObj(theaterObj)
    distanceStr = ""
    if distance >= 1000:
        distanceStr = '{:.2f}Km'.format(distance/1000)
    else:
        distanceStr = '{}m'.format(distance)
    theaterInfoEle.update({'distance':distanceStr})
    return theaterInfoEle

def GetMovieScheduleInfoByObj(moviescheduleObj):
    movieScheduleEle = {
        'room':moviescheduleObj.room,
        'totalSeat':moviescheduleObj.totalSeat,
        'availableSeat':moviescheduleObj.availableSeat,
        'startTime':'{:02}:{:02}'.format(int(moviescheduleObj.startTime/100), moviescheduleObj.startTime%100),
        'endTime': '{:02}:{:02}'.format(int(moviescheduleObj.endTime/100), moviescheduleObj.endTime%100),
        'subtitle':moviescheduleObj.subtitle,
        'dubbing':moviescheduleObj.dubbing,
        'roomProperty':moviescheduleObj.roomProperty
    }
    return movieScheduleEle

def GetMovieScheduleList(reqtheater, movieID):
    movieScheduleList = []
    movieSchedules = MovieSchedules.objects.filter(theater__exact=reqtheater.id, movie__exact=movieID)
    for movieSchedule in movieSchedules:
        movieScheduleDict = {
            'room':movieSchedule.room,
            'totalSeat':movieSchedule.totalSeat,
            'availableSeat':movieSchedule.availableSeat,
            'startTime':'{:02}:{:02}'.format(int(movieSchedule.startTime/100), movieSchedule.startTime%100),
            'endTime': '{:02}:{:02}'.format(int(movieSchedule.endTime/100), movieSchedule.endTime%100),
            'subtitle':movieSchedule.subtitle,
            'dubbing':movieSchedule.dubbing,
            'roomProperty':movieSchedule.roomProperty
        }
        movieScheduleList.append(movieScheduleDict)
    return movieScheduleList


class TimeOrderedSchedule:
    def __init__(self, movie, movieScheduleList):
        self.movie = movie
        self.movieSchedule = movieScheduleList
    
    def GetJson(self):
        TimeOrderSchduleJSON = GetMovieInfoByObj(self.movie)

        timeScheduleList = []
        for movieScheduleObj in self.movieSchedule:
            timeScheduleDict = GetMovieScheduleInfoByObj(movieScheduleObj)
            theaterObj = Theaters.objects.get(id=movieScheduleObj.theater)
            theaterInfo = GetTheaterInfoByObj(theaterObj)
            timeScheduleDict.update({'theaterInfo':theaterInfo})
            timeScheduleList.append(timeScheduleDict)

        TimeOrderSchduleJSON.update({'timeschedule':timeScheduleList})
        return TimeOrderedSchedule

    



class TheaterOrderedSchedule:
    def __init__(self, movie, theater):
        self.movie = movie
        self.theater = theater
    
    def movieUpdate(self, movie):
        self.movie = movie

    def theaterUpdate(self, theater):
        self.theater = theater


    def GetJson(self):
        movieDict = GetMovieInfoByObj(self.movie)
        
        theaterList = []
        for theater in self.theater:
            theaterInfo = GetTheaterInfoByObj(theater['theaterInfo'])
            distanceStr = ""
            if theater['distance'] >= 1000:
                distanceStr = '{:.2f}Km'.format(theater['distance']/1000)
            else:
                distanceStr = '{}m'.format(theater['distance'])
            theaterInfo.update({'distance':distanceStr})
            theaterEle = {
                'theaterInfo':theaterInfo,
                'theaterSchedule':theater['theaterSchedule']
            }
            theaterList.append(theaterEle)
        
        TOSJson = {
            'movie':movieDict,
            'theater':theaterList
        }

        return TOSJson
        

    
