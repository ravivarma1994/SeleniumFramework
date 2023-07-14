from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()
driver.switch_to.frame("frm1")
