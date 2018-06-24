#这个文件用来实现一个登录功能的自动化操作
# 表示注释
import time
from selenium import webdriver
#从谷歌公司的一个项目导入网络驱动，用代码来操作浏览器
driver = webdriver.Chrome()
#driver=webdriver.Firefox()
#设置隐式等待,如果页面中的元素在20秒内找到，一旦找到页面元素马上执行后面语句，如果超过20秒，仍然找不到页面元素，那么程序依然报超时错误
# 隐式等待方法在脚本中只写以此即可
driver.implicitly_wait(20)
#1.打开浏览器
#2.打开海盗商城网站
driver.get(" http://172.31.15.27:8081/") # 输入这个网址也可以 http://localhost/
#3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#4.输入用户名称和密码
driver.find_element_by_id("username").send_keys("lyy")
driver.find_element_by_name("password").send_keys("1101ocs.!")
#5.点击登录按钮
#所有调用的方法都会有提示，没有提示信息就表示没有该方法
driver.find_element_by_class_name("login_btn").click()
#6.检查登录是否成功
#导入包的快捷键 Alt+Enter
#time.sleep() 这个方法提供了一种固定的时间等待，这里的意思是点击登录按钮后等待5秒后再检查用户名称是否正常
#弊端是因为网络延迟，所以并不清楚需要等待多长时间比较合适
#因此可以用智能等待替换固定等待
#time.sleep(10)
username_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
#通过if语句判断页面显示的文本是否一致，判断测试用力是否执行成功
print(username_text)
#if username_text=='您好 lyy':
#    print("测试执行通过")
#else:
#    print("测试执行失败 ")
#selenium主要用于回归测试，所以脚本刚开始都是pass的，只有开发变更代码。一般工作中不用判断语句
#7.点击进入商场购物按钮
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
#Xpath有一个缺陷，定位元素的可读性比较差
driver.find_element_by_link_text("进入商城购物").click()
#8.在商城主页输入搜索条件“iphone”
driver.find_element_by_name("keyword").send_keys("iphone")
#9.点击搜索按钮
driver.find_element_by_class_name("btn1").click()
time.sleep(10)
#10.点击第一个商品图片
#driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img").click() 通过图片进入
driver.find_element_by_link_text("苹果 (Apple) iPhone 6 (A1586) 16GB 金色 移动联通电信4G手机").click() #通过文本链接进入
time.sleep(5)
#11.点击“加入购物车”
driver.switch_to.window(driver.window_handles[-1])
time.sleep(10)
#driver.find_element_by_link_text("加入购物车").click()   ?为什么不对
driver.find_element_by_class_name("goods-add").click()
driver.close()  #关闭窗口



