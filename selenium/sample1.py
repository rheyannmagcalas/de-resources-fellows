import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
sleep(random.randint(12, 18))

target_page = "https://www.rappler.com/topic/covid-19/"
driver.get(target_page)

options = Options()
# options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

### Browser Details
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.quit()
