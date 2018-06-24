#1.登录海盗商城
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("http://localhost")
# driver.find_element_by_link_text("登录").click()
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
# driver.find_element_by_id("username").send_keys("lyy")
# actions=ActionChains(driver)
# actions.send_keys(Keys.TAB).send_keys("1101ocs.!").perform()
# actions.send_keys(Keys.ENTER).perform()
import time
from selenium import webdriver
#文件名称、类名、包名都应该与字母开头，可以有数字和下划线，但是不允许有空格和中文
from day2.loginTest import Login
driver=webdriver.Chrome()
#implicitly_wait主要是用于监测页面的加载时间，什么时候加载完成，什么时候执行后置操作
driver.implicitly_wait(20)
#实例化对象会占用内存，pycharm会自动释放内存，代码运行完，检测到
#Login()这个对象不再被使用，所以自动释放，因此关闭了页面
#创建好一个空白浏览器后，或许所有的操作都在这个浏览器中执行
Login().loginWinthDefaultUser(driver)
#2.点击“账号设置”   本来要使用driver这个变量，但是现在文件中没有driver变量
driver.find_element_by_link_text("账号设置").click()
#3.点击“个人资料”
#partial_link_text可以使用链接的一部分元素定位，放链接文本过长时，推荐使用partial_link_text方法定位元素，使用该方法时，可以用链接中的任意部分只要这部分是唯一的即可
#Xpath的方法比较通用，可以用工具自动生成，但是不推荐使用（可读性较差），逼不得已时使用
driver.find_element_by_link_text("个人资料").click()
#driver.find_element_by_partial_link_text("个人资料").click()
#4.修改真实姓名
#如果文本框中有内容时，需要先清空，再进行输入；可以再send_keys之前都加入一个clear操作。
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("张三")
#5.修改性别
#单选框中name与ID都一致时，保密，男，女的区别为value值不同，可以通过value值定位元素，使用value定位元素有两种方法：Xpath和CSS_selector两种方法
#t通过find_element_by_css_selector方法定位元素时，只需要在唯一属性的两边增加中括号即可
#driver.find_element_by_css_selector('[value="2"]').click()
#在Xpath中//双斜线表示采用相对路径定位元素，相对路径一般通过元素的特殊属性查找元素
# /单斜线表示绝对路径，一般都是从/HTML根节点开始定位元素，一般通过元素的位置与层级关系查找元素
#绝对路径比较长，涉及到的父节点比较对，代码稳定行比较差（当页面布局发生变化后，影响的可能行较大）
#相对路径，查询速度慢，因为需要遍历更对的节点，工作中推荐使用find_element_by_css_selector方法，该方法查询速度快
#*号表示任意节点，[@]表示通过属性定位
#driver.find_element_by_xpath('//*[@value="1"]').click()
#也可以通过JavaScript的getElementByClassName（）方法找到页面上符合条件的所有元素
#如果要查找页面上的所有元素就用find_elements方法，如果是查找页面上的唯一元素就用find_element方法。
driver.find_elements_by_id("xb")[0].click()
#6.修改生日
#一下一下点年月日是可以实现的，但是稳定性比较差，涉及太多的元素定位，很容易选错，并且很难修改日期，尽量不用Click（）点击日期
#因为readonly属性，所以无法使用send_keys（）方法修改日期
#driver.find_element_by_id("date").clear()
#driver.find_element_by_id("date").send_keys("2011-01-01")
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("2011-01-01")
#7.修改QQ
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("1234567890")
#8.点击确定，保存成功\
driver.find_element_by_class_name("btn4").click()
time.sleep(3)
driver.switch_to.alert.accept()
