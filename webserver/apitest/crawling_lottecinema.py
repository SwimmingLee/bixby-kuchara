'''
megabox 영화관별로 정보가져오기2

영화이름, 상영등급, 상영종류, 상영관, 시작 시간, 끝나는 시간, 남은 좌석, 총 좌석 등을
한 번에 가져와서 뿌려보기
'''
'''
크롤링한 데이터를 json으로 받아와보자
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
import re
import sys

driverDir = r'C:\\chromedriver_win32\\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=driverDir, chrome_options=options)


detailDivisionCode = "1"
cinemaID = "1004"

url = 'http://www.lottecinema.co.kr/LCHS/Contents/Cinema/Cinema-Detail.aspx?divisionCode=1&detailDivisionCode={}&cinemaID={}'.format(detailDivisionCode, cinemaID)
driver.get(url)
time.sleep(2)
req = driver.page_source
bs = BeautifulSoup(req, 'html.parser')

movieSchedule = bs.find('div', {'class':re.compile('time_aType .*')})
movieLists = movieSchedule.findAll('dl', {'class':re.compile('time_line .*')})
for movieList in movieLists:
    movieRating = movieList.find('span', {'class':re.compile('grade_.*')})
    print(movieRating.text)
    movieName = movieRating.next_sibling
    print(movieName)
    movieScreens = movieList.findAll('dd', {'class':re.compile('screen.*')})
    for movieScreen in movieScreens:
        movieTheaterTimes = movieScreen.find('ul', {'class':re.compile('theater_time *')}).findAll('li', recursive=False)
        for movieTheaterTime in movieTheaterTimes:
            movieRoom = movieTheaterTime.find('span', {'class':re.compile('cineD.*')})
            print(movieRoom.text)
            movieTime = movieTheaterTime.find('span', {'class':'clock'})
            print(movieTime.text)
            movieSeatInfo = movieTheaterTime.find('span', {'class':'ppNum'})
            if movieSeatInfo != None:
                print(movieSeatInfo.text)
            else:
                print("[ERROR] 32/32")
