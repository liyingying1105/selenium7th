#实现自动化注册功能
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(" http://172.31.15.27:8081/")
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("lyy1")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("15210289242")
driver.find_element_by_name("email").send_keys("yy1105yy@163.com")
driver.find_element_by_class_name("reg_btn").click()
