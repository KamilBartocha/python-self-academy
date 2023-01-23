from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://justjoin.it")
# driver.close()
print(driver.title)
driver.quit()