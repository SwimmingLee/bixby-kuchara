'''
megabox 영화관별로 정보가져오기2
​
영화이름, 상영등급, 상영종류, 상영관, 시작 시간, 끝나는 시간, 남은 좌석, 총 좌석 등을
한 번에 가져와서 뿌려보기
'''
'''
크롤링한 데이터를 json으로 받아와보자
지금 보니까 테이블이 없으면 에러가 난다.
에러처리하는 함수를 만들어 주자. 가능하면 try catch를 사용할 것!
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.request
import time
import json
import re
import sys
from .models import Movies
from .models import MovieSchedules
from .update import GetMovieInfo
import datetime

def WebDriverInit():
    global driver
    #driverDir = r'C:\Users\student\works\chromedriver_win32\chromedriver.exe'
    driverDir = r'C:\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=driverDir, chrome_options=options)


def MegaBoxCrawl(theaterObj):
    movieJson = ""
    movieObj = ""
    movieList = []
    movieDict = dict()
    print(theaterObj.theaterName)

    legacyMovieSchedules = MovieSchedules.objects.filter(theater=theaterObj)
    legacyMovieSchedules.delete()

    region = theaterObj.regionCode
    cinema = theaterObj.theaterCode

    url = 'http://megabox.co.kr/?menuId=theater-detail&region={}&cinema={}'.format(region,cinema)
    driver.get(url)

    req = driver.page_source
    bs = BeautifulSoup(req, 'html.parser')

    movieScedule = bs.find('div', {'class':'timetable_container'})
    movieTableRow = movieScedule.find('tbody')
    if movieTableRow == None:
        # 여기에 들어왔다는 것은 현재 상영중인 영화가 없다는 뜻이다.
        return None
    movieTableRow = movieTableRow.findAll('tr')
    

    for row in movieTableRow:
        movieName = row.find('a', {'title':'영화상세 보기'})
        if movieName != None:
            movieNameStr = movieName.text
            p = re.compile("\[(.*)\] ")
            m = p.match(movieNameStr)
            if m:
                movieNameStr = movieNameStr.replace(m.group(), '')
            
            p = re.compile("\((.*)\) ")
            m = p.match(movieNameStr)
            if m:
                movieNameStr = movieNameStr.replace(m.group(), '')
                if m.group() == '(더빙) ':
                    movieDict['dubbing'] = True
            else:
                movieDict['dubbing'] = False
                    
            
            movieNameStr = movieNameStr.strip()
            movieDict['movieName'] = movieNameStr
            

            # movieName을 primary key로 변경하면 get으로 변경
            movieObj = Movies.objects.filter(movieName=movieNameStr)
            movieObj = movieObj.first()
            if movieObj == None:
                movieObj = GetMovieInfo(movieNameStr)      

        movieRoomInfo = row.find('th', {'class':'room'})
        movieRoom = movieRoomInfo.find('div')
        if movieRoom != None:            
            movieRoomStr = movieRoom.text
            movieDict['room'] = movieRoomStr
        
        movieSubtitle = movieRoomInfo.find('small')
        if movieSubtitle != None:
            subtitleIdx = movieSubtitle.text.find('자막')
            
            if subtitleIdx > 0:
                movieDict['subtitle'] = True
            else:
                movieDict['subtitle'] = False

        movieCinemaTimes = row.findAll('div', {'class':re.compile('^cinema_time')})
        
        for movieCinemaTime in movieCinemaTimes:
            movieTime = movieCinemaTime.find('span', {'class':'hover_time'})
            movieStartTimeStr = ""
            movieEndTimeStr = ""
            if movieTime != None:
                movieTimeStr = movieTime.text
                movieStartTimeStr, movieEndTimeStr = movieTimeStr.split('~')
                movieDict['startTime'] = movieStartTimeStr
                movieDict['endTime'] = movieEndTimeStr
            else:
                print("[ERROR]: not found moive time")
                print(movieTime)


            movieTimeInfo = movieCinemaTime.find('p', {'class':re.compile("time_info.*")})
            movieSeatInfo = movieTimeInfo.find('span', {'class':'seat'})
            if movieSeatInfo != None:
                movieSeatInfoStr = movieSeatInfo.text
                try:
                    avaliableSeat, totalSeat = movieSeatInfoStr.split('/')
                except:
                    avaliableSeat = "-1"
                    totalSeat = "-1"
                    
                movieDict['avaliableSeat'] = avaliableSeat
                movieDict['totalSeat'] = totalSeat

                hour, minute = movieDict['startTime'].split(':')
                startTime  = int(hour)*100 + int(minute)

                hour, minute = movieDict['endTime'].split(':')
                endTime  = int(hour)*100 + int(minute)

                MovieScheduleEle = MovieSchedules(movie=movieObj, theater=theaterObj, room=movieDict['room'], \
                                    totalSeat=totalSeat, availableSeat=avaliableSeat, dubbing=movieDict['dubbing'], \
                                    startTime=startTime, endTime=endTime, subtitle=movieDict['subtitle'])
                MovieScheduleEle.save()
                movieJson = json.dumps(movieDict, ensure_ascii=False)
                movieList.append(movieJson)
    return movieList
    #return movieDict

