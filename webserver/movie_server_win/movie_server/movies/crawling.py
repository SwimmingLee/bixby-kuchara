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
import copy
from .models import Movies
from .models import MovieSchedules
from .update import GetMovieInfo

from datetime import datetime


def WebDriverInit():
    global driver
    #driverDir = r'C:\Users\student\works\chromedriver_win32\chromedriver.exe'
    #driverDir = r'/home/ubuntu/Downloads/chromedriver'
    driverDir = r'C:\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=driverDir, chrome_options=options)


def MovieCrawl(theaterObj):
    diffTime = GetDiffTime(theaterObj.updatedTime, datetime.now())    
    print(diffTime)
    if (diffTime > 60*15):
        if theaterObj.brand == 'megabox':
            MegaBoxCrawl(theaterObj)
        elif theaterObj.brand == 'lottecinema':
            LotteCinemaCrawl(theaterObj)
        elif theaterObj.brand == 'cgv':
            CGVCrawl(theaterObj)
        theaterObj.updatedTime = datetime.now()
        theaterObj.save() 


def CGVCrawl(theaterObj):   
    movieObj = ""
    movieList = []
    movieDict = dict()
    print(theaterObj.theaterName)

    legacyMovieSchedules = MovieSchedules.objects.filter(theater=theaterObj)
    legacyMovieSchedules.delete()

    region = theaterObj.regionCode
    cinema = theaterObj.theaterCode 
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode={}&theatercode={}&date=20191010'.format(region, cinema)
    driver.get(url)

    req = driver.page_source
    bs = BeautifulSoup(req, 'html.parser')

    movieSchedule = bs.find('div', {'class':'sect-showtimes'}).find('ul')

    movieScheduleLists = movieSchedule.findAll('li', recursive=False)

    for movieScheduleList in movieScheduleLists:
        #movieRating = movieList.find('span', {'class':re.compile('ico-grade.*')})
        #print(movieRating.text.strip())
        movieName = movieScheduleList.find('strong')
        movieNameStr = movieName.text.strip().replace('-', ':').strip()
        #print(movieNameStr)
        #print(type(movieNameStr))
        movieDict['movieName'] = movieNameStr
        
        movieObj = Movies.objects.filter(movieName=movieNameStr)
        movieObj = movieObj.first()
        if movieObj == None:
            movieName = movieName.encode('utf-8')
            #print(type(movieName))
            movieObj = GetMovieInfo(movieName)
            if movieObj == None:
                continue 

        movieHallTypes = movieScheduleList.findAll('div', {'class':'type-hall'})
        for movieHallType in movieHallTypes:
            movieType = movieHallType.ul.find('li')
            SoundX = False
            if movieType.text.find('더빙') >= 0:
                movieDict['dubbing'] = True
            else:
                movieDict['dubbing'] = False
            if movieType.text.find('SOUNDX') >= 0:
                SoundX = True
            #print(movieType.text.strip())

            movieRoom = movieType.next_sibling.next_sibling
            #print(movieRoom.text.strip())
            movieRoomStr = movieRoom.text.strip() 
            movieDict['room'] = movieRoomStr
            if movieRoomStr.find('IMAX') >= 0:
                movieDict['roomProperty'] = 'IMAX'
            elif movieRoomStr.find('SCREENX') >= 0:
                movieDict['roomProperty'] = 'SCREENX'
            elif movieRoomStr.find('STARIUM') >= 0:
                movieDict['roomProperty'] = 'STARIUM'
            elif movieRoomStr.find('SphereX') >= 0:
                movieDict['roomProperty'] = 'SphereX'
            elif movieRoomStr.find('GOLD CLASS') >= 0:
                movieDict['roomProperty'] = 'GOLD CLASS'
            elif movieRoomStr.find('CINE de CHEF') >= 0:
                movieDict['roomProperty'] = 'CINE de CHEF'
            elif movieRoomStr.find('TEMPUR CINEMA') >= 0:
                movieDict['roomProperty'] = 'TEMPUR CINEMA'
            elif movieRoomStr.find('PREMIUM') >= 0:
                movieDict['roomProperty'] = 'PREMIUM'
            elif movieRoomStr.find('SUBPAC ') >= 0:
                movieDict['roomProperty'] = 'SUBPAC '
            elif movieRoomStr.find('씨네앤리빙룸') >= 0:
                movieDict['roomProperty'] = '씨네앤리빙룸'
            elif movieRoomStr.find('ART') >= 0:
                movieDict['roomProperty'] = 'ART'
            elif movieRoomStr.find('SKYBOX') >= 0:
                movieDict['roomProperty'] = 'SKYBOX'


            totalSeat = movieRoom.next_sibling.next_sibling
            totalSeatStr = re.findall("\d+", totalSeat.text)[0]
            #movieDict['totalSeat'] = int(totalSeatStr)

            movieTimeLists = movieHallType.find('div', {'class':'info-timetable'}).findAll('li')
            for movieTimeList in movieTimeLists:
                startTime = movieTimeList.find('em')
                hour, minute = startTime.text.split(':')
                movieDict['startTime'] = int(hour)*100 + int(minute)
                hourcarry = int(minute) + movieObj.duration + 10
                movieDict['endTime'] = (int(hour) + int(hourcarry / 60) ) * 100 + hourcarry % 60

                availableSeat = startTime.next_sibling
                if availableSeat.text.find("마감") >= 0 or availableSeat.text.find("매진") >= 0:
                    movieDict['availableSeat'] = -1
                    movieDict['totalSeat'] = -1
                else:
                    availableSeatStr = re.findall("\d+", availableSeat.text)[0]
                    movieDict['availableSeat'] = int(availableSeatStr)
                    movieDict['totalSeat'] = int(totalSeatStr)

                MovieScheduleEle = MovieSchedules(movie=movieObj, theater=theaterObj, room=movieDict['room'], \
                                    totalSeat=movieDict['totalSeat'], availableSeat=movieDict['availableSeat'], dubbing=movieDict['dubbing'], \
                                    startTime=movieDict['startTime'], endTime=movieDict['endTime']
                                )
                MovieScheduleEle.save()
                movieList.append(copy.copy(movieDict))
    return movieList



def LotteCinemaCrawl(theaterObj):
    movieObj = ""
    movieList = []
    movieDict = dict()
    print(theaterObj.theaterName)

    legacyMovieSchedules = MovieSchedules.objects.filter(theater=theaterObj)
    legacyMovieSchedules.delete()

    region = theaterObj.regionCode
    cinema = theaterObj.theaterCode

    url = 'http://www.lottecinema.co.kr/LCHS/Contents/Cinema/Cinema-Detail.aspx?divisionCode=1&detailDivisionCode={}&cinemaID={}'.format(region, cinema)
    
    driver.get(url)

    '''
    alert = driver.switch_to_alert()
    if alert != None:
        alert.accept()
    '''
    time.sleep(2)
    req = driver.page_source
    bs = BeautifulSoup(req, 'html.parser')

    movieSchedule = bs.find('div', {'class':re.compile('time_aType .*')})
    movieScheduleLists = movieSchedule.findAll('dl', {'class':re.compile('time_line .*')})
    for movieScheduleList in movieScheduleLists:
        movieRating = movieScheduleList.find('span', {'class':re.compile('grade_.*')})
        #print(movieRating.text)
        movieName = movieRating.next_sibling.strip()
        movieDict['movieName'] = movieName
        movieObj = Movies.objects.filter(movieName=movieName)
        movieObj = movieObj.first()
        if movieObj == None:
            movieObj = GetMovieInfo(movieName)
            if movieObj == None:
                continue  

        movieScreens = movieScheduleList.findAll('dd', {'class':re.compile('screen.*')})
        for movieScreen in movieScreens:
            movieCineD1 = movieScreen.find('ul', {'class':'cineD1'}).findAll('li')
            movieDict['subtitle'] = False
            movieDict['dubbing'] = False
            for cineD1 in movieCineD1:
                if cineD1.text.find('자막') >= 0:
                    movieDict['subtitle'] = True
                elif cineD1.text.find('더빙') >= 0:
                    movieDict['dubbing'] = True 
                elif cineD1.text.find('슈퍼플렉스 G') >= 0:
                    movieDict['roomProperty'] = '슈퍼플렉스 G'
                elif cineD1.text.find('슈퍼 S') >= 0:
                    movieDict['roomProperty'] = '슈퍼 S'
                else:
                    movieDict['roomProperty'] = '2D'

            movieTheaterTimes = movieScreen.find('ul', {'class':re.compile('theater_time *')}).findAll('li', recursive=False)
            for movieTheaterTime in movieTheaterTimes:
                movieRoom = movieTheaterTime.find('span', {'class':re.compile('cineD.*')})
                movieDict['room'] = movieRoom.text
                if movieRoom.text.find('샤롯데 프라이빗'):
                    movieDict['roomProperty'] = '샤롯데 프라이빗'
                elif movieRoom.text.find('샤롯데'):
                    movieDict['roomPropery'] = '샤롯데'

                # print(movieRoom.text)
                movieTime = movieTheaterTime.find('span', {'class':'clock'})
                startTimeStr, endTimeStr = movieTime.text.split('~')

                hour, minute = startTimeStr.split(':')
                if hour.find('심야') >= 0:
                    movieDict['lateNight'] = True
                    movieDict['morning'] = False
                    hour = hour.replace('심야', '')
                elif hour.find('조조') >= 0:
                    movieDict['lateNight'] = False
                    movieDict['morning'] = True
                    hour = hour.replace('조조', '')
                else:
                    movieDict['lateNight'] = False
                    movieDict['morning'] = False
                movieDict['startTime'] = int(hour)*100 + int(minute)

                hour, minute = endTimeStr.split(':')
                movieDict['endTime'] = int(hour)*100 + int(minute)

                #print(movieTime.text)
                movieSeatInfo = movieTheaterTime.find('span', {'class':'ppNum'})
                if movieSeatInfo != None:
                    if movieSeatInfo.text.find('마감') >= 0 or movieSeatInfo.text.find('매진') >= 0:
                        movieDict['avaliableSeat'] = -1
                        movieDict['totalSeat'] = -1
                    else:    
                        avaliableSeatStr, totalSeatStr = movieSeatInfo.text.split('/')
                        movieDict['avaliableSeat'] = re.findall('\d+', avaliableSeatStr)[0]
                        movieDict['totalSeat'] = re.findall('\d+', totalSeatStr)[0]
                    #print(movieSeatInfo.text)
                
                MovieScheduleEle = MovieSchedules(movie=movieObj, theater=theaterObj, room=movieDict['room'], \
                                    totalSeat=movieDict['totalSeat'], availableSeat=movieDict['avaliableSeat'], dubbing=movieDict['dubbing'], \
                                    startTime=movieDict['startTime'], endTime=movieDict['endTime'], subtitle=movieDict['subtitle'], \
                                    lateNight=movieDict['lateNight'], morning=movieDict['morning']
                                )
                MovieScheduleEle.save()
                movieList.append(copy.copy(movieDict))
    return movieList


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
            if movieRoomStr.find('MX') >= 0:
                movieDict['roomProperty'] = 'MX'
            elif movieRoomStr.find('컴포트') >= 0:
                movieDict['roomProperty'] = '컴포트'
            elif movieRoomStr.find('더부티크') >= 0:
                if movieRoomStr.find('스위트룸') >= 0:
                    movieDict['roomProperty'] = '더부티크S'
                else:
                    movieDict['roomProperty'] = '더부티크'
            else:
                movieDict['roomProperty'] = '2D'
        
        movieSubtitle = movieRoomInfo.find('small')
        if movieSubtitle != None:
            if movieSubtitle.text.find('자막') >= 0:
                movieDict['subtitle'] = True
            else:
                movieDict['subtitle'] = False
            if movieSubtitle.text.find('필름소사이어티') >= 0:
                movieDict['roomProperty'] = movieSubtitle.text


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

