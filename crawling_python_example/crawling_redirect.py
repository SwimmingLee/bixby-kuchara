from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

options = webdriver.ChromeOptions()
options.add_argument('headless')
driverDir = r'C:\Users\student\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverDir, chrome_options=options)
url = 'http://pythonscraping.com/pages/javascript/redirectDemo1.html'
driver.get(url)
waitForLoad(driver)
print(driver.page_source)

