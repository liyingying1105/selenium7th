#用unittest写一个后台登录的测试用例
#1.导包
import unittest

import time
from selenium import webdriver
#2建类，并继承unittest.TestCase
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class LoginTest(unittest.TestCase):
    #3.重写setup和teardown
    @classmethod
    def setUpClass(self):
        #4.打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #窗口最大化的代码，要求驱动版本必须和浏览器精准匹配
        self.driver.maximize_window()
    #4个空格，在pycharm中可以用tab键代替
    @classmethod
    def tearDownClass(self):
#    为了保证可以看清测试结果，增加一个30秒的延时等待
        time.sleep(30)
#   测试案例执行完成后，应把打开的浏览器关闭，释放内存，清楚cookie和缓存，为下次执行测试用例准备。局部变量不允许被其他方法访问的。把setUp（）方法中声明driver改成全局变量
#       self代表类，在局部变量增加self.    表示这个变量属于这个类
        self.driver.quit()
    def test_login(self):
        #使用driver时前面都要加self.,为了简化代码可以把成员变量self.driver赋值给局部变量driver
        driver=self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        #常用键转义字符代替，\t表示tab键      \n表示enter键
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()
    def test_product_adding(self):
        driver=self.driver
        #如果第二个方法重新打开一个浏览器，登录就无效了
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        #除了用name属性切换frame ，也可以通过巴中元素定位方法定位元素，然后切换
        iframe=driver.find_element_by_id("mainFrame")
        driver.switch_to.frame(iframe)
        driver.find_element_by_name("name").send_keys("饮水机")
        #变量名文件名的起名规则：数字，大小写字母，下划线，一般要求以字母开头.如果id是纯数字，用#号的方式不能定位，可以用[]的方式定位，所有的属性都可以用[]定位
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_id("2").click()
        driver.find_element_by_id("6").click()
        #driver.find_element_by_id("7").click()
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        select=Select (driver.find_element_by_name("brand_id"))
        select.select_by_value("1")
        driver.find_element_by_class_name("button_search").click()


if __name__ == '__main__':
    unittest.main()