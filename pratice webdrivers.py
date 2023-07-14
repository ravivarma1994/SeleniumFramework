import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver.get("https://www.google.com/")
driver.get("https://www.functionize.com/free-trial?utm_source=google&utm_medium=paid%2Bsearch&utm_campaign=free-trial&utm_term=automated%20web%20testing&utm_campaign=Z+-+India+-+Automated+Web+Testing&utm_source=adwords&utm_medium=ppc&hsa_acc=5488573823&hsa_cam=16375912712&hsa_grp=133300773506&hsa_ad=583785827749&hsa_src=g&hsa_tgt=kwd-304942589907&hsa_kw=automated%20web%20testing&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad=1&gclid=Cj0KCQjw4s-kBhDqARIsAN-ipH2ef1zlTcDKpAiM1JwZ04ik4GwbFqYNEv6jJr9CEQNrZNadzQ70SSYaAjOiEALw_wcB")

drop = driver.find_element(By.XPATH,"//*[@id='job_role-46e27199-313a-4a78-bd72-b85b29dd0158']")
drp=Select(drop)
drp.select_by_visible_text("Other")

drop2=driver.find_element(By.XPATH,"//*[@id='total_size_of_test_suite-46e27199-313a-4a78-bd72-b85b29dd0158']")
drp=Select(drop2)
drp.select_by_visible_text("501-1000")
time.sleep(2)


time.sleep(10)