# open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

s = Service("chromedriver.exe") # add relative path of chromedriver make sure the version matches your chrome browser
driver = webdriver.Chrome(options=options, service=s)

driver.get("http://google.com")
time.sleep(2)

# fetch the search input box using xpath

user_input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')

user_input.send_keys('CampusX')
time.sleep(4)

user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div[1]/div/a')
link.click()
time.sleep(1)

link = driver.find_element(by=By.XPATH, value='//*[@id="1668425005116"]/span[2]/a')
link.click()
