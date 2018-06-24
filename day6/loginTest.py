

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("lyy")
driver.find_element_by_name("password").send_keys("1101ocs.!")
driver.find_element_by_class_name("login_btn").click()
 #因为中间存在一个“登录成功的页面”，所以不能直接点击该链接
#三种解决办法：time sleep（）；隐式等待；显示等待
 #显示等待的如下：
#WebDriverWait(driver,20,0.5).until(expected_condition)
#WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT, "进入商城购物")))
WebDriverWait(driver,20, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,"进入商城购物")))
#这句显示等待的代码相当于time.sleep（20）的优化版本
driver.find_element_by_link_text("进入商城购物").click()