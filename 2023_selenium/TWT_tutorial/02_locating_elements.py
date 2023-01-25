from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# search order: id -> class -> name
# Task: search "test" in search bar and print summary of all results from
# website https://techwithtim.net.

driver = webdriver.Chrome()
driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-summary")
        print(header.text)
finally:
    driver.quit()
