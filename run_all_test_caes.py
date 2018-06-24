#用来批量执行unittest的测试用例，是这个测试工作的唯一入口
#1.导入unittest，批量执行测试用例功能由unittest代码库提供
import smtplib
import unittest
import os
from email.mime.text import MIMEText
from package.HTMLTestRunner import HTMLTestRunner
def send_mail(path):
    #1.通过path打开新生成的测试报告文件，HTML不是文本格式，需要指定二进制的方式打开
    file=open(path,'rb')
    #2.读取文件的内容，作为邮件正文
    msg=file.read()
    #3.把读取出的内容转换成MIMEText的格式
    mime=MIMEText(msg, _subtype='html', _charset='utf-8')
    #4.设置主题和发件人，收件人
    mime['subject']='lyy自动化测试报告'
    #因为发件人需要登录密码，这里的密码不是真正的密码，是客户端授权码 第三方不能直接用密码，必须用授权码
    mime['from']='bwftest126@126.com'
    to='yy1101yy@163.com'
    mime['To']=to
    #1.实现SMTP（）构造方法
    smtp=smtplib.SMTP()
    #2.链接126邮箱
    smtp.connect("smtp.126.com")
    #3.登录126邮箱
    smtp.login('bwftest126@126.com', 'abc123asd654')
    #4.发送邮箱
    #to_addrs=smtp.send_Message()
    #smtp.sendmail(mime,from_addr='bwftest126@126.com', to_addrs='yy1105yy@163.com')
    smtp.sendmail(from_addr='bwftest126@126.com', to_addrs=to, msg=mime.as_string())
    #5.退出
    smtp.quit()

if __name__ == '__main__':
    #2.批量执行授权要明确你要执行那些测试用例
    #智能执行继承了unittest.TestCase是类
    #执行这个项目中所有unittest的测试用例
    #defaultTestLoader 默认的测试用例加载器，discover（）发现
    # 可以用来发现所有的测试用例
    #*表示统配符，可以代替任何符号，*Test.py结尾的所有文件
    #.表示当前路径，即项目的根目录     suite表示变量名，测试用例集
    suite=unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #执行所有测试用例
    #suite=unittest.defaultTestLoader.discover('.', pattern='*.py')
    #3.执行测试用例
    #unittest.TextTestRunner().run(suite)
    #4.生成测试报告 HTMLTestRunner类似于TextTestRunner，都是批量执行测试用例的，区别在于他们执行完所有测试用例的输入，一个是Text，一个是HTML
    #Text 打印在控制台中，HTML会单独生成一个文件，相比于Text，HTML结构更加清晰
    #HTMLTestRunner().run(suite)代替 unittest.TextTestRunner().run(suite)
    #5.定义测试报告的保存路径
    base_path=os.path.dirname(__file__)
    path=base_path+'/report/test_report.html'
    #6.创建文件
    file=open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="lyy测试报告", description="测试环境：server 2088;浏览器：谷歌").run(suite)
    #7.把测试报告作为邮件发送，优势：及时提醒。
    send_mail(path)