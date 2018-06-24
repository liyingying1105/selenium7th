#这种框架的设计思想叫page-object设计模式，是一种高级的框架设计思想，主旨是把业务逻辑和代码技术分离开，测试用例的类主要负责业务逻辑，网页对象类主要负责元素定位和操作。在pageObject这个类中，把每个网页看成一个类。其中网页中的每个元素看成类中的属性。针对这个元素的操作，看成类中的一个方法。
#元素的信息定位是名词性的，所以可以看成属性（成员变量）。元素的操作是动词性的，所以是看成是方法
from selenium import webdriver

#这个类主要做的就是把元素定位改一个易于理解的名字
from selenium.webdriver.common.by import By


class LoginPage:
    #为这个网页创建一个构造函数,构造函数固定名称 __init__（）
    def __init__(self,driver):
        #因为setUP中已经创建了一个浏览器，所以初始化方法时不需要新建浏览器，直接用setUP建好的浏览器
        #self.driver=webdriver.Chrome()
        self.driver=driver
        self.url="http://localhost/index.php?m=user&c=public&a=login"
    #python的元组，类似于数组,这句话的意思是声明了一个数组叫username_input_loc，数组中包含两个元素，分别是ID和username
    username_input_loc=(By.ID,"username")
    password_input_loc=(By.ID,"password")
    login_btn_loc=(By.CLASS_NAME,"login_btn")
    def open(self):
        self.driver.get(self.url)

    #给参数设置默认值，如果调用方法时，传入一个新的用户名，那么使用信息
    #如果调用方法时，不传入参数，那么使用默认值
    def input_username(self,usernaem='lyy'):
        #类中涉及到三个元素定位，因为元素定位不太稳定，经常需要修改，所以应该把定位方式声明成勒种的一个属性
        #self.driver.find_element(By.ID,"username").send_keys(usernaem)
        #*号表示find_element（）这个方法传入的不是一个元组，而是把元组中的每个元素都分别传入find_element（）这个方法，作为单独参数
        self.driver.find_element(*self.username_input_loc).send_keys(usernaem)
    def input_password(self,password='1101ocs.!'):
        #self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login_button(self):
        #self.driver.find_element_by_class_name("login_btn").click()
        self.driver.find_element(*self.login_btn_loc).click()