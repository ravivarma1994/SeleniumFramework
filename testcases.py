import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://login.yahoo.com/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "phone-no").send_keys("vegesnaravivarma@yahoo.com")
time.sleep(2)
driver.find_element(By.ID, "login-signin").click()
time.sleep(4)
driver.find_element(By.ID, 'login-passwd').send_keys("ravi4@varma")
time.sleep(10)
driver.find_element(By.ID, "login-signin").click()
time.sleep(10)
