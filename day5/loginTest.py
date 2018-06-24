import unittest

import time

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这个类不需要再写setup和tearDown方法，只需要写测试用例的方法即可
    def test_login(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("lyy")
        driver.find_element_by_id("password").send_keys("1101ocs.!")
        old_title=driver.title
        driver.find_element_by_class_name("login_btn").click()
        time.sleep(5)
        new_title=driver.title
        print("旧页面"+old_title)
        print(new_title)
        self.assertNotEqual(old_title,new_title)
        #print(driver.title)
        print(driver.current_url)

if __name__ == '__main__':
    unittest.main()