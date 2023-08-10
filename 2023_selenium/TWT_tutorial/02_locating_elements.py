from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# search order: id -> class -> name
# Task: search "test" in search bar and print summary of all results from
# website https://techwithtim.net.

driver = webdriver.Chrome()
driver.get("https://techwithtim.net")
time.sleep(5)
print(driver.title)

search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


