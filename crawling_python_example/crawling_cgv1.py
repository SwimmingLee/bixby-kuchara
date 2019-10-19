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


areaCode = "01"
theatherCode = "0011"


url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode={}&theatercode={}&date=20191010'.format(areaCode, theatherCode)
# url = 'http://megabox.co.kr/?menuId=theater-detail&region=30&cinema=4431'
driver.get(url)

#element = driver.findElement(By.className("sect-showtimes"))
#print(element.page_source)
req = driver.page_source
bs = BeautifulSoup(req, 'html.parser')

# print(bs)


#theaterSchedule > div.timetable_container
movieSchedule = bs.find('div', {'class':'sect-showtimes'}).find('ul')
# print(movieSchedule)

movieLists = movieSchedule.findAll('li', recursive=False)
# print(movieLists)
for movieList in movieLists:
    movieRating = movieList.find('span', {'class':re.compile('ico-grade.*')})
    print(movieRating.text.strip())
    movieName = movieList.find('strong')
    print(movieName.text.strip())
    movieHallTypes = movieList.findAll('div', {'class':'type-hall'})
    for movieHallType in movieHallTypes:
        movieType = movieHallType.ul.find('li')
        print(movieType.text.strip())

        movieRoom = movieType.next_sibling.next_sibling
        print(movieRoom.text.strip())

        totalSeat = movieRoom.next_sibling.next_sibling
        print(totalSeat.text.replace(" ", "").replace('\n', ''))

        movieTimeLists = movieHallType.find('div', {'class':'info-timetable'}).findAll('li')
        for movieTimeList in movieTimeLists:
            startTime = movieTimeList.find('em')
            print(startTime.text)

            availableSeat = startTime.next_sibling
            if (availableSeat.text != "마감"):
                movieNightType = availableSeat["class"]
                print(movieNightType)
            print(availableSeat.text)

    

'''
movieTableRow = movieShcedule.find('tbody').findAll('tr')

print(sys.stdout.encoding)
movieDict = dict()

for row in movieTableRow:
    movieName = row.find('a', {'title':'영화상세 보기'})
    if movieName != None:
        movieNameStr = movieName.text
        #print(movieNameStr)
    
    movieRating = row.find('span', {'class':re.compile("age_m age_[0-9.*].*")})
    if movieRating != None:
        movieRatingStr = movieRating.text
        #print(movieRatingStr)
    
    movieRoom = row.find('th', {'class':'room'}).find('div')
    if movieRoom != None:
        movieRoomStr = movieRoom.text
        #print(movieRoomStr)
    
    movieTimeInfos = row.findAll('p', {'class':re.compile("time_info.*")})
    for movieTimeInfo in movieTimeInfos:
        movieHover = movieTimeInfo.previous_sibling
        print(movieHover)
        # movieTimeStr = movieHover.text
        # print(movieTimeStr)
        movieStartTime = movieTimeInfo.find('span', {'class':'time'})
        if movieStartTime != None:
            movieStartTimeStr = movieStartTime.text
            #print(movieStartTimeStr)
        movieSeatInfo = movieTimeInfo.find('span', {'class':'seat'})
        if movieSeatInfo != None:
            movieSeatInfoStr = movieSeatInfo.text
            #print(movieSeatInfoStr)
            movieDict['movieName'] = movieNameStr
            movieDict['movieRating'] = movieRatingStr
            movieDict['startTime'] = movieStartTimeStr
            movieDict['room'] = movieRoomStr
            movieDict['seatInfo'] = movieSeatInfoStr
            movieJson = json.dumps(movieDict)
            print(movieDict)
            #print(movieJson)
'''
