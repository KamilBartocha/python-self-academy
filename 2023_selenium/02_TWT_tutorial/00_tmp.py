from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()

ENDPOINT = "https://techwithtim.net"
driver.get(ENDPOINT)
print(driver.title)
sleep(3)
python_tile = driver.find_element(By.CLASS_NAME, "tag__TagContainer-sc-3f52y0-0 fPNUsx")
python_tile.click()
