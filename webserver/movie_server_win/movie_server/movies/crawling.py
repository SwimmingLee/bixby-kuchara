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
from .update import GetMovieInfo

def WebDriverInit():
    global driver
    driverDir = r'C:\Users\student\works\chromedriver_win32\chromedriver.exe'
    # driverDir = r'C:\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=driverDir, chrome_options=options)


def MegaBoxCrawl(regionCode, theaterCode):
    movieJson = ""
    movieList = []
    movieDict = dict()

    region = regionCode
    cinema = theaterCode

    url = 'http://megabox.co.kr/?menuId=theater-detail&region={}&cinema={}'.format(region,cinema)
    driver.get(url)

    req = driver.page_source
    bs = BeautifulSoup(req, 'html.parser')

    movieScedule = bs.find('div', {'class':'timetable_container'})
    movieTableRow = movieScedule.find('tbody').findAll('tr')

    for row in movieTableRow:
        movieName = row.find('a', {'title':'영화상세 보기'})
        if movieName != None:
            movieNameStr = movieName.text
            movieDict['movieName'] = movieNameStr
            # filter를 쓰지 않고 get으로 에러를 검사하면
            # 데이터를 확인 할 수 있을 것임.
            movieObj = Movies.objects.filter(movieName=movieNameStr)
            movieObj = movieObj.first()
            if movieObj == None:
                GetMovieInfo(movieNameStr)
            
        #print(movieNameStr)

        # 영화에 대한 정보는 DB에서 추출해서 사용할 것임
        '''    
        movieRating = row.find('span', {'class':re.compile("age_m age_[0-9.*].*")})
        if movieRating != None:
            movieRatingStr = movieRating.text
            movieDict['movieRating'] = movieRatingStr
        #print(movieRatingStr)
        '''

        movieRoom = row.find('th', {'class':'room'}).find('div')
        if movieRoom != None:
            movieRoomStr = movieRoom.text
            movieDict['room'] = movieRoomStr
            
        #print(movieRoomStr)

        movieTime = row.find('div', {'class':'cinema_time'}).find('a')
        movieStartTimeStr = ""
        movieEndTimeStr = ""
        if movieTime != None:
            movieTimeStr = movieTime.text
            movieStartTimeStr, movieEndTimeStr = movieTimeStr.split('~')
            movieDict['startTime'] = movieStartTimeStr
            movieDict['endTime'] = movieEndTimeStr

        movieTimeInfos = row.findAll('p', {'class':re.compile("time_info.*")})
        for movieTimeInfo in movieTimeInfos:
            movieSeatInfo = movieTimeInfo.find('span', {'class':'seat'})
            if movieSeatInfo != None:
                movieSeatInfoStr = movieSeatInfo.text
                try:
                    avaliableSeat, totalSeat = movieSeatInfoStr.split('/')
                    movieDict['avaliableSeat'] = avaliableSeat
                    movieDict['totalSeat'] = totalSeat
                except:
                    movieDict['avaliableSeat'] = "-1"
                    movieDict['totalSeat'] = "-1"
                
                movieJson = json.dumps(movieDict, ensure_ascii=False)
                movieList.append(movieJson)
    return movieList
    #return movieDict

