
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

target_page = "https://www.gmanetwork.com/news/sports/"
driver.get(target_page)
driver.maximize_window()


options = Options()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
sleep(3)


title = driver.find_elements(By.XPATH, '//a[@class="story_link story"]')

for _title in title:
    print(_title.text)
    print(_title.get_attribute('href'))


