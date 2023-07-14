import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/?tag=msndeskabkin-21&ref=pd_sl_5szpgfto9j_e&adgrpid=1320515071595367&hvadid=82532451009254&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=155423&hvtargid=kwd-82533067351416:loc-90&hydadcr=14452_2154372")
driver.maximize_window()
driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()
driver.find_element(By.ID,"ap_email").send_keys(9985034322)
driver.find_element(By.ID,"continue").click()
time.sleep(2)
driver.find_element(By.ID,"ap_password").send_keys("Anil@123")
t1 = driver.find_element(By.ID,"auth-signin-button").click()

time.sleep(3)
#driver.find_element(By.XPATH,"//*[@id='searchDropdownBox']/option[1]").click()
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("soaps")
time.sleep(5)
driver.find_element(By.ID,("nav-search-submit-button")).click()
time.sleep(5)