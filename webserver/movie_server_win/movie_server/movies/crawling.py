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

def WebDriverInit():
    global driver
    driverDir = r'C:\Users\student\works\chromedriver_win32\chromedriver.exe'
    # driverDir = r'C:\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=driverDir, chrome_options=options)


def GetMovieInfo(movieName):
    client_id = "Ob9m_EHdGWkXlNLSWPjo"
    client_key = "tA5WWOMJHo"
    url = "https://openapi.naver.com/v1/search/movie.json"
    option = "&display=1&sort=count"
    query = "?query="+urllib.parse.quote(movieName)
    url_query = url + query + option
    #Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_key)
    #검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        movieInfo = response_body.decode('utf-8')
        # print(movieInfo)
        movieInfo = json.loads(movieInfo)
        link = movieInfo["items"][0]["link"]
        imgUrl = movieInfo["items"][0]["image"]
        actor = movieInfo["items"][0]["actor"]
        director = movieInfo["items"][0]["director"]
        userRating = movieInfo["items"][0]["userRating"]

        print("imgUrl: " + imgUrl)
        print("actor: " + actor)
        print("director: " + director)
        print("userRating: " + userRating)

        MoviesEle = Movies(movieName=movieName, director=director, actor=actor, movieRating="...", duration=120, genre="...", userRating=userRating, imgUrl=imgUrl)
        MoviesEle.save()
    else:
        print("Error code:"+rescode)



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
            # filter를 쓰지 않고 get으로 에러를 검사하면
            # 데이터를 확인 할 수 있을 것임.
            movieObj = Movies.objects.filter(movieName=movieNameStr)
            movieObj = movieObj.first()
            # print(type(movieObj))
            # print(movieObj)
            if movieObj == None:
                # print("None!!!!")
                GetMovieInfo(movieNameStr)
            
        #print(movieNameStr)
    
        movieRating = row.find('span', {'class':re.compile("age_m age_[0-9.*].*")})
        if movieRating != None:
            movieRatingStr = movieRating.text
        #print(movieRatingStr)
    
        movieRoom = row.find('th', {'class':'room'}).find('div')
        if movieRoom != None:
            movieRoomStr = movieRoom.text
        #print(movieRoomStr)

        movieTime = row.find('div', {'class':'cinema_time'}).find('a')
        movieStartTimeStr = ""
        movieEndTimeStr = ""
        if movieTime != None:
            movieTimeStr = movieTime.text
            movieStartTimeStr, movieEndTimeStr = movieTimeStr.split('~')

        movieTimeInfos = row.findAll('p', {'class':re.compile("time_info.*")})
        for movieTimeInfo in movieTimeInfos:
            movieSeatInfo = movieTimeInfo.find('span', {'class':'seat'})
            if movieSeatInfo != None:
                movieSeatInfoStr = movieSeatInfo.text

                movieDict['movieName'] = movieNameStr
                movieDict['movieRating'] = movieRatingStr
                movieDict['startTime'] = movieStartTimeStr
                movieDict['endTime'] = movieEndTimeStr
                movieDict['room'] = movieRoomStr
                movieDict['seatInfo'] = movieSeatInfoStr
                movieJson = json.dumps(movieDict, ensure_ascii=False)
                movieList.append(movieJson)
    return movieList
    #return movieDict

