from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker")
time.sleep(3)

cookies_button = driver.find_element(By.LINK_TEXT, "Got it!")
cookies_button.click()
language_select = driver.find_element(By.ID, "langSelect-EN")
language_select.click()
time.sleep(5)

# # productPrice1 -> productPrice0
# items = list(driver.find_element(By.ID, "productPrice0"))
# items.append(driver.find_element(By.ID, "productPrice1"))

for i in range(5000):
    cookie_count = driver.find_element(By.ID, "cookies")
    cookie = driver.find_element(By.ID, "bigCookie")
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
    count = cookie_count.text
    print(count)

#TODO write upgrades

time.sleep(4)