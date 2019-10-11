'''
megabox 영화관별로 정보가져오기2

영화이름, 상영등급, 상영종류, 상영관, 시작 시간, 끝나는 시간, 남은 좌석, 총 좌석 등을
한 번에 가져와서 뿌려보기
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driverDir = r'C:\Users\student\Downloads\chromedriver_win32\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=driverDir, chrome_options=options)

url = 'http://megabox.co.kr/?menuId=theater-detail&region=10&cinema=1372'
driver.get(url)
theaterScheduleField = driver.find_elements_by_id('theaterSchedule')


req = driver.page_source
bs = BeautifulSoup(req, 'html.parser')

movieNames = bs.findAll('a', {'title': '영화상세 보기'})
for movieName in movieNames:
    print(movieName)

theaterRooms = bs.findAll('th', {'class':'room'})
for theaterRoom in theaterRooms:
    print(theaterRoom)

print(theaterScheduleField)



