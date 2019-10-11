'''
megabox 영화관별로 정보가져오기
megabox 홈페이지에서 셀레니움을 통해 좌석정보 가져왔다. (예약완료, 일반석, 장애인석 등 구분 가능/ 
좌석 정보는 픽셀단위 그대로 json형식으로 뿌려주면 pillow를 통해 이미지를 만들 수 있을 것이다.)

그 이외도 영화이름, 상영등급, 상영종류, 상영관, 시작 시간, 끝나는 시간, 남은 좌석, 총 좌석 등을
크롤링할 수 있는 것을 확인하였다. 


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
# theaterScheduleField = driver.find_elements_by_id('theaterSchedule')

# 크롬에서 xpath를 이용하면 쉽게 구현할 수 있다. 
seatPos = driver.find_element_by_xpath('//*[@id="theaterSchedule"]/div[2]/table/tbody/tr[1]/td/div[1]/a')
driver.execute_script("arguments[0].click();", seatPos)

time.sleep(3)
seatChk = driver.find_element_by_xpath('//*[@id="messageBox7"]/div/div[3]/button')
seatChk.send_keys('\n')
time.sleep(3)
print(driver.page_source)
# time.sleep(5)
req = driver.page_source
bs = BeautifulSoup(req, 'html.parser')

seatInfo = bs.findAll('div', {'class':'seat_wrap'})

print(seatInfo)
# print(driver.page_source)

'''
req = driver.page_source
bs = BeautifulSoup(req, 'html.parser')

movieNames = bs.findAll('a', {'title': '영화상세 보기'})
for movieName in movieNames:
    print(movieName)

theaterRooms = bs.findAll('th', {'class':'room'})
for theaterRoom in theaterRooms:
    print(theaterRoom)

print(theaterScheduleField)
'''


