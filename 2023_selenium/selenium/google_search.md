### Kolejność szukania elementów

search order: id -> class -> name


#### Import modułu selenium oraz time
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *
```

#### Wybranie webdrivera do konkretnej przeglądarki
``` driver = webdriver.Safari()```

#### Załadowanie strony do aktualnej sesji

```driver.get("https://google.com")```

#### wyświetlenie tutułu strony pobranej za pomocą get

```print(driver.title)```

#### Zaakceptowanie ustawień(otwieramy przeglądarkę pierwszy raz)
```
accept_all = driver.find_element(By.ID, "L2AGLb")
accept_all.click()
```
#### Znalezienie pola wyszukiwarki, wpisanie "selenium test" oraz kliknięcie enter(RETURN)
```
search = driver.find_element(By.ID, "APjFqb")
search.send_keys("selenium test")
search.send_keys(Keys.RETURN)
```
#### Znalezienie pola "result-stats"
``` results = driver.find_element(By.ID, "result-stats") ```

#### Oczekiwanie że results nie jest puste
``` assert results.text is not None ```

#### Zamknięcie przeglądarki i sesji załadowanej strony
```driver.quit()```

#### całość razem

```commandline
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *

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

```