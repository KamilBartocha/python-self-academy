#### Import modułu selenium:

```from selenium import webdriver```

#### Wybranie webdrivera do konkretnej przeglądarki
``` driver = webdriver.Safari()```

#### Załadowanie strony do aktualnej sesji

```driver.get("https://codebrainers.pl/")```

#### wyświetlenie tutułu strony pobranej za pomocą get

```print(driver.title)```

#### Zamknięcie przeglądarki i sesji załadowanej strony
```driver.quit()```