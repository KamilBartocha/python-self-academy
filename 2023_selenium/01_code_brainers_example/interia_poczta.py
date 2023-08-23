from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *

driver = webdriver.Safari()
driver.get("https://poczta.interia.pl/logowanie")
sleep(5)
print(driver.title)
# Akceptacja RODO
go_to_service = driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
go_to_service.click()
sleep(5)
# Wpisywanie nazwy e-mail
input_email = driver.find_element(By.ID, "email")
input_email.send_keys("code.brainers.tester@interia.pl")
sleep(5)
# Wpisywanie hasła
input_password = driver.find_element(By.ID, "password")
input_password.send_keys("testerZAQ!2wsx")
sleep(5)

# Kliknięcie Zaloguj się
button_log_in = driver.find_element(By.CLASS_NAME, "btn")
button_log_in.click()
sleep(10)

print(driver.title)
assert driver.title == "Poczta w Interii"
sleep(10)
driver.quit()
