import  unittest

import time
from tabnanny import check

from  selenium import webdriver
#2.继承unittest.testcase
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4



class RegisterTest(unittest.TestCase):
    #3.重写setup和teardown方法
    @classmethod
    def setUp(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDown(cls):
        time.sleep(30)
        cls.driver.quit()

    #4.编写测试用例，以test开头的方法
    def test_register(self):
        for row in CsvFileManager4().read('test_data.csv'):
            driver=self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            #find_element(),下面两种方法没有任何区别，但是第二种方法扩展性更好，便于数据库封装
            #driver.find_element_by_name("username")
            driver.find_element(By.NAME,"username").send_keys(row[0])
            driver.find_element(By.NAME,"password").send_keys(row[1])
            driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
            driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
            driver.find_element(By.NAME, "email").send_keys(row[4])
            #driver.find_element(By.CLASS_NAME,"reg_btn").click()
            #for循环中执行测试用例，虽然解决了批量执行的问题，但是如果第一行数据就失败了，后续的测试用还会不会被执行  考虑异常情况输入完邮箱后，按tab键，检查提示信息是否都是“通过信息验证”
            check_tip=driver.find_element(By.CSS_SELECTOR," form> ul > li:nth-child(1) > div > span").text
            print(check_tip)
            #其中check_tip是执行用历史从网页上抓取的实际结果，“通过信息验证”是来自与手工测试用，是在测试用例执行前的期望结果，
            #if check_tip=="通过信息验证":
             #   print("测试通过")
            #else:
             #   print("测试失败")
             #   #通过if else语句可以自动判断测试用例的执行情况
            self.assertEqual("通过信息验证",check_tip)


if __name__ == '__main__':
    unittest.main()