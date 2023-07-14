from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://www.google.com/")
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,"a")



print("Number of links:",len(links))
i=1;
for link in links:
    if link.is_displayed():
        print("Link",i, ":", link.text)
    i+=1
