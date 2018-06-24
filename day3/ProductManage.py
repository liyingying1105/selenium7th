#1.登录后台
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("userverify").submit()
#2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
#3.点击添加商品
driver.find_element_by_link_text("添加商品").click()
#4.输入商品名称
#driver.find_element_by_css_selector("body > div.content > div.install.tabs.mt10 > dl > form > dd:nth-child(1) > ul > li:nth-child(1) > input").send_keys("iphone")
#操作子框架中的元素，首先要进行frame切换
driver.switch_to.frame('mainFrame')
driver.find_element_by_name("name").send_keys("iphone")
#5.选择商品分类（双击或者“选择当前分类”）

#6.在下拉框中选择商品品牌
dropdown4=driver.find_element_by_name("brand_id")
Select(dropdown4).select_by_visible_text("苹果")
#7.点击提交按钮
#driver.find_element_by_class_name("button_search").click()
#编辑代码：找出第一个不能实现的部分16
