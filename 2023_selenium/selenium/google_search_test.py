from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

# GIVEN "test selenium" is typed into search on google.com
# WHEN ENTER is presses (search request)
# THEN Result stats are calculated and visible on screen

driver = webdriver.Safari()
driver.get("https://google.com")
sleep(10)

button_accept = driver.find_element(By.ID, "L2AGLb")
button_accept.click()
sleep(10)

search_form = driver.find_element(By.ID, "APjFqb") #ID pola wyszukiwarki: APjFqb
search_form.send_keys("test selenium")
search_form.send_keys(Keys.ENTER)
sleep(10)

result_stat = driver.find_element(By.ID, "result-stats") # div ze statystykami: result-stats
assert result_stat.text is not None

sleep(10)







# results_number = re.search(r"(About \d+)", result_stat.text)
# sleep(3)
# results_number = results_number[0][6:]
# print(results_number)


# button_accept = driver.find_element(By.CLASS_NAME, "x")
# button_accept = driver.find_element(By.NAME, "y")