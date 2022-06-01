import bs4
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# sleep(random.randint(12, 18))

target_page = "https://www.rappler.com/topic/covid-19/"
driver.get(target_page)
driver.maximize_window()



options = Options()
# options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

driver.implicitly_wait(5)


total_height = int(driver.execute_script("return document.body.scrollHeight"))
available_links = []
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))

page_source = driver.page_source
soup = bs4.BeautifulSoup(page_source, 'lxml')

data = soup.select('div#primary > article > div.archive-article__content')
for _data in data:
    
    link_info = _data.select('h2 > a')
    if len(link_info) > 0:
        print('URL', link_info[0]['href'])
        print('Title', link_info[0].text.strip())

        time_info = _data.find('time')
        print('Time', time_info.text.strip())


driver.quit()



