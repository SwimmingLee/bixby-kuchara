from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument('headless')
driverDir = r'C:\Users\student\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverDir, chrome_options=options)
url = 'http://pythonscraping.com/pages/javascript/redirectDemo1.html'
driver.get(url)

try:
    bodyElement = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located(
        (By.XPATH, '//body[contains(text(), "This is the page you are looking for!")]')
    ))
    print(bodyElement)
except TimeoutException:
    print("Did not find the element")