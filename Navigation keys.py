import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.facebook.com/")
print(driver.title)
driver.find_element(By.XPATH,"//*[@id='u_0_5_ay']").click()
driver.back()

print(driver.title)
time.sleep(3)
driver.forward()
print(driver.title)
time.sleep(3)
