from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
i=1
for link in links:
    if link.text.strip():
        print(i,link.text.strip())
        i+=1


