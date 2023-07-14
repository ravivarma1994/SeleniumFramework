import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
time.sleep(2)
dropdown = driver.find_element(By.XPATH,"//select[@class='col-lg-3'and @id='first']").click()
drp = Select(dropdown)
drp.select_by_visible_text("Yahoo")
time.sleep(5)


