from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *

# search order: id -> class -> name
# Task: search "selenium test" in search bar and print result stats(Except not empty)
# website https://google.com.

driver = webdriver.Safari()
driver.get("https://google.com")
sleep(5)
print(driver.title)

accept_all = driver.find_element(By.ID, "L2AGLb")
accept_all.click()
sleep(5)

search = driver.find_element(By.ID, "APjFqb")
search.send_keys("selenium test")
sleep(5)

search.send_keys(Keys.RETURN)
sleep(5)

results = driver.find_element(By.ID, "result-stats")
print(results.text)
assert results.text is not None
sleep(5)
driver.quit()
