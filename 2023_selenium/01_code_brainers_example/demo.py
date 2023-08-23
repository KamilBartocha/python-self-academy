from selenium import webdriver
import time

driver = webdriver.Safari()
driver.get("https://codebrainers.pl/")
time.sleep(10)
print(driver.title)
driver.quit()
