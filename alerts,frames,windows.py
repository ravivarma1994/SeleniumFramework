import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver.get("https://www.google.com/")
driver.maximize_window()
#driver.get("https://demoqa.com/alerts")
#driver.find_element(By.XPATH,"//button[@id='alertButton'and@class='btn btn-primary']").click()

#driver.switch_to.alert.accept()
#time.sleep(5)

