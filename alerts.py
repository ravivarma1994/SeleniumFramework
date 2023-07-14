import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")

driver.find_element(By.XPATH,"//*[@id='OKTab']/button").click()




