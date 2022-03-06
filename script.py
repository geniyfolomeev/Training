from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.python.org/')
driver.find_element(By.CSS_SELECTOR, '#id-search-field').send_keys("selenium")
driver.find_element(By.CSS_SELECTOR, '#id-search-field').send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()