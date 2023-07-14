import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']").click()
driver.find_element(By.XPATH,"//input[@id='ap_email']").send_keys("vegesnaravivarma@yahoo.com")
driver.find_element(By.XPATH,"//input[@id='continue'and@class='a-button-input']").click()
driver.find_element(By.XPATH,"//input[@id='ap_password'and@name='password']").send_keys("ravi4@varma")
driver.find_element(By.ID,"signInSubmit").click()
driver.find_element(By.NAME,"field-keywords").send_keys("soap")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.XPATH,"//span[text()='Top Brands']").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/span/div/div[3]/div/div/div/div/div/div/div/div/h2/a/span").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
drop = driver.find_element(By.XPATH,"//select[@name='quantity'and@id='quantity']")
drp = Select(drop)
drp.select_by_visible_text("3")
time.sleep(2)
driver.find_element(By.NAME,"submit.add-to-cart").click()
time.sleep(2)




time.sleep(5)

