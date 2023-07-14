import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']").click()
#Action=ActionChains(driver)
#Action.move_to_element(By.XPATH,"//div[@id='nav-flyout-ya-newCust']/a").click()
#driver.find_element(By.XPATH,"//div[@class='nav-line-1-container']/following-sibling::span")
driver.find_element(By.ID,"createAccountSubmit").click()
driver.find_element(By.NAME,"customerName").send_keys("ravivarma")
driver.find_element(By.XPATH,"//div[@class='a-fixed-left-grid-col a-col-right']/input").send_keys("9676181218")
driver.find_element(By.XPATH,"//div[@class='a-row a-spacing-micro']/input").send_keys("vegesnaravivarma@yahoo.com")
driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys("ravi4@varma")
driver.find_element(By.CLASS_NAME,"a-button-input").click()
time.sleep(10)