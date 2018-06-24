#第一个单元测试框架的示例
#1.要想用Unittest框架，首先导入包,但是unittest不需要解压或安装。unittest比selenium更常用，几乎所有测试都要用unittest组织测试，所以Python把unittest集成在Python的SDK中了，因此不需要单独下载和安装，unittest是Python内置的代码库
import unittest
#2.创建类，用来编写自动化测试用例，该类需要继承unittest框架中testcase。一个类就为一个测试用例
#Python中的类名最好和文件名不一样 ()表示继承，继承是值自雷完全继承父类的所有方法和属性，并且有自己的扩展内容
class FirstUnitTest(unittest.TestCase):
#    3.重写父类的setUp和tearDown方法。这两个方法在每次执行时都会执行一次
    def setUp(self):
#        set up()方法是在测试用例方法执行之前要做的操作，类似于手工测试中的预置条件
         print(1)
    def tearDown(self):
#        tearDown()实在测试用例方法执行之后要做的操作，比如可能需要还原测试场景，或者清除脏数据
        print(2)  #前面要有8个空格
    def test_login(self):
#        这个方法用来编写测试步骤
#       框架规定：测试用例方法必须以test开头,只有以test开头飞方法才会被当做测试用例执行
        print(3)
    def switch_window(self):
#       窗口切换方法只是希望被调用才能执行,这个方法不是test开头，所以无法直接允许，只有被调用时运行
        print(4)
    def test_zhuce(self):
        #在Python中，类里面的每个方法都有一个默认参数，叫self，类似与Java中的this关键字，代表类本身，如果你想使用类的属性和方法，那么必须在调用方法的前面家self关键字。
        #根据光标所在的位置，决定执行什么测试用例，光标在那个方法中，那么就会只执行那个测试用例，当光标在unittest.main()中时，就会执行所有的测试用例
        self.switch_window()
    #也可以选择重启setupclass和teardownClass方法
#了解即可，不常用
    @classmethod   #只在类中所有方法前后执行一次。在Python中叫装饰器，在Java中叫注解
    def setUpClass(cls):
        print(5)
    @classmethod
    def tearDownClass(cls):
        print(6)

#这是一个固定写法，在程序运行之前通过这句话可以自动判断当前文件是不是程序的入口
#如果当前文件是程序的入口，那么就会执行if子句中的内容
if __name__ == '__main__':
    #unittest.main()可以理解为当前文件的主函数，会自动调用类中的所有测试用例方法
    unittest.main()

#一个类中，所有测试用例方法的执行顺序是根据方法名的字母顺序进行执行

