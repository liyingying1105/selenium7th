#封装方法，使用时直接调用，Python中的类关键字与Java一样CLSS
#python中方法也有一个关键字，是def define的缩写，定义方法



#1.打开浏览器

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
#Python中使用冒号代替大括号，在冒号后点击回车自动缩进4个空格，所有属于这个类中的语句都必须空4个空格
class Login:
    '''def代表这是一个方法   loginWinthDefaultUser 方法名称    方法后面的括号用来声明参数    self 表示类本事，类似与Java中的this关键字
    方法声明的后面也有冒号，所以方法声明后面也要缩进四个空格    ctrl+/也可以整段注释
    #直接封装法法也可以，可以把类去掉'''
    def loginWinthDefaultUser(self,driver):
        #driver = webdriver.Chrome()
        #2.打开海盗商城
        driver.get("http://localhost")
        #3.删除登录链接的target属性
        #在Python中字符串可以用单引号，也可以用双引号，如果引用的字符串中包含双引号时，那么引用单引号即可
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        #4.点击登录按钮，跳转到登录页面
        driver.find_element_by_link_text("登录").click()
        #5.不弹出新的登录窗口，输入用户名
        driver.find_element_by_id("username").send_keys("lyy")
        #6.输入密码
        #导入ActionChains包 alt+Enter
        #action 动作行为   Chains 时链表的意思   链表类似与数组   ActionChains是一组动作行为的的意思
        #下面这句话的作用是实例化一个ActionChains这个类的对象，这个对象可以用来执行一组动作和行为
        #和Java的区别就是去掉了new关键字
        #ActionChains actions=ActionChains(drivrt)  这句话有问题，Python语言中实例化对象不需要声明变量类型
        actions=ActionChains(driver)
        # 如果要使用键盘上的任意控件，直接去keys这个类中找
        #所有actions中的方法必须以perform()结尾才会被执行
        #ActionChains(drivrt).send_keys(Keys.TAB).send_keys("1101ocs.!").perform()
        actions.send_keys(Keys.TAB).send_keys("1101ocs.!").perform()
        #drivrt.find_element_by_id("password").send_keys("1101ocs.!")
        #7.点击登录按钮
        #ActionChains(drivrt).send_keys(Keys.ENTER)
        #actions.send_keys(Keys.ENTER).perform()
        #如果回车键不支持登录，可以直接点击登录按钮
        #如果也不能定位登录按钮，还可用Submit（）方法  ，用于提交表单
        #同时提交多个信息时可以用其中的任何一个元素来执行Submit（）方法来提交表单中的所有数据
        # 例如，使用户名来提交表单
        driver.find_element_by_id("username").submit()
