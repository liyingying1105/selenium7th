#1.iphone打开主页
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(" http://172.31.15.27:8081/")
#2.点击登录按钮
driver.find_element_by_link_text("登录").click()
#3.在搜索框中输入

#进行窗口切换 driver.switch_to.window("")
driver.switch_to.window("")
#selenium提供了所有窗口名字的集合  handles句柄的意思，句柄理解为名字即可
#driver.window_handles 可以理解为数组
#[1]代表数组的第二个元素
#driver.window_handles[1]
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_name("keyword").send_keys("iphone")
#[1]表示第二个元素，[-1]表示最后一个元素，所以也可以把1改为-1
#在python中元组和列表可以正着从0开始数，也可以负着从-1开始数，倒数第二个为-2 以此类推