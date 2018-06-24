#selenium执行Javascript中的两个关键字：return（返回值）和arguments(参数)
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost")
driver.implicitly_wait(20)
#点击"登录"链接  JavaScript的方法： 用document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium的方法找登录链接代码
#driver.find_element_by_link_text("登录")
#某些元素，用selenium的方法找元素比JavaScript更容易，虽然selenium不支持remoceAttribute的JavaScript方法，但是selenium找到登录链接和JavaScript找到的是同一个元素
#可以用selenium找到元素后转换成JavaScript的元素，这样写JavaScript就比较容易一点，不需要childNodes方法。例如：
#driver.find_element_by_link_text("登录").removeAttribute()
login_link=driver.find_element_by_link_text("登录")
#把原来的JavaScript看成一个无参无返回值的方法，现在直接从外面传入一个页面元素，就变成了一个有参无返的方法
#把selenium找到的这个元素，传入到JavaScript方法里，代替原来的JavaScript定位
#arguments参数的复数形式，[0]表示第一个参数，指的是js后面的login_link
#arguments是参数数组，指的是js字符串后面的所有参数。一般只用的arguments[0]，即为字符串的第一个参数
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
#输入用户名和密码
driver.find_element_by_id("username").send_keys("lyy")
ActionChains(driver).send_keys(Keys.TAB).send_keys("1101ocs.!").send_keys(Keys.ENTER).perform()
#返回商城首页
driver.find_element_by_link_text("返回商城首页").click()
#搜索iPhone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#点击商品（用这用方法，在实现一次不打开新窗口)
#因为img没有target属性，收益以复制css的时候找他的父节点
#找到需要删除的target属性的标签并给一个命名，单css往往比较长，可以适当缩减他的长度，点位元素的目标节点是最后一个节点，>号的前面是父节点，后面为子节点，每个节点的第一个单词是标签名，比如a,div,body。每个小数点后面表示class属性。nth-child(2),nth表示第几个，child表示子节点
product_link_css="div.protect_con > div > div.shop_01-imgbox > a"
#使用JavaScript删除a标签的target属性
iPhone=driver.find_element_by_css_selector(product_link_css)
#通过Xpath定位元素
#删除元素的target属性
driver.execute_script("arguments[0].removeAttribute('target')",iPhone)
iPhone.click()
#点击加入购物车
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_css_selector(".shopCar_T_span3").click()
#点击结算按钮
#用find_element_by_css_selector（）方法时前面增加小数点，去掉中间的空格，就可以同时用两个属性定位元素
driver.find_element_by_css_selector(".shopCar_btn_03").click()
#点击添加新地址
driver.find_element_by_class_name("add-address").click()
#输入收货人信息（选择地区是难点）
#收货人
driver.find_element_by_name("address[address_name]").send_keys("千玺")
#手机号
driver.find_element_by_name("address[mobile]").send_keys("12548963547")
#driver.find_element_by_id("document.getElementById('add-new-area-select')[1]")
#下拉框是一种特殊的网页元素，对下拉框的操作和普通网页元素不太一样，selenium为这种特殊的元素，专门创建了一个类 Select
#收货地址
dropdown1=driver.find_element_by_id("add-new-area-select")
#dropdown1的类型是一个普通网页元素，把一个普通的网页元素，转换成一个下拉框的特殊网页元素
#print(type(dropdown1))#dropdown1为web_element类型
#web_element类中，只有click和send_Keys的方法，没有下拉框选项的方法
select1=Select(dropdown1)
#print(type(select1))#select1是select类型，转换成select类型后，网页元素没有变化，select类中有选择选项的方法
#select1.select_by_value("320000")#通过选项的值定位
time.sleep(2)
select1.select_by_visible_text("辽宁省")#可以通过选项的文本信息定位
time.sleep(3)
#因为是动态Id,所以无法通过ID来定位元素，因为class重复，所以也无法通过class定位，可以通过find_element的方法，找到页面中所有class=add-new-area-select的元素，然后通过下表的方式选择第n个页面元素，类似JavaScript方法
dropdown2=driver.find_elements_by_class_name("add-new-area-select")[1]
#select2=Select(dropdown2)
Select(dropdown2).select_by_visible_text("沈阳市")
#dropdown3=driver.find_elements_by_class_name("add-new-area-select")[-1]
#find_elements_by_tag_name()这个方法大多数情况都能找到一堆元素，所以find_element_by_tag_name（）这个方法很少用，find_elements_by_tag_name（）比较常用
dropdown3=driver.find_elements_by_tag_name("select")[2]
Select(dropdown3).select_by_visible_text("和平区")


#详细地址
driver.find_element_by_name("address[address]").send_keys("解放大街123号")
#邮政编码
driver.find_element_by_name("address[zipcode]").send_keys("100000")
#document.getElementById("add-new-area-select")[1]
#点击保存收货人地址
driver.find_element_by_class_name("aui_state_highlight").click()