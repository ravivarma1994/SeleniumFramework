import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://login.yahoo.com/?.intl=in')
driver.find_element(By.ID,"login-username").send_keys("srinivas_pasem")
time.sleep(3)
driver.find_element(By.NAME,"signin").click()
time.sleep(3)
driver.find_element(By.ID,"login-passwd").send_keys("9348204445")
time.sleep(3)
driver.find_element(By.NAME,"verifyPassword").click()
time.sleep(10)
