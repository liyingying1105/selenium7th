#1.导包
import csv

import os

#声明方法
class CsvFileManager4:
    def read(self,filename):
        list=[]#声明一个空列表
        #2.指定CSV文件的路径
       # path=r"C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv" #缺点：可移植性较差，项目切换路径后就得修改代码
        #更好的方法如下
        #base_parh=os.path.dirname(__file__)固定写法，用来获取当前文件的目录结构，OS表示操作系统，path表示路径 dirname表示目录名，__file__是Python内置的变量，表示当前文件  C:/Users/51Testing/PycharmProjects/selenium7th/day5
        base_parh=os.path.dirname(__file__)
        print(base_parh)
        #用base_path的好处：不管项目放在任何路径下，都可以找到该文件的绝对路径，利用绝对路径计算CSV文件的路径
        path=base_parh.replace('day5','data/'+filename)
        print(path)
        #3.打开指定文件
       # file=open(path,'r')
        #每次打开文件用完之后关闭该文件，释放系统资源，用try...finally的方法，更常用的方法是with...as的语法结构
        with open(path,'r') as file:
            data_table=csv.reader(file)
            #4.循环遍历数据表中的每一行
            for row in data_table:
                print(row)
        #测试用例需要调用这些数据，所以要给这个方法设一个返回值，把数据提取出来 5.声明一个二维列表，保存data_table中的所有数据
                list.append(row)
                #在read方法的末尾，返回这个列表
        return list
    #一个CSV文件只适合保存

#if __name__=='__main__':
 #   list = CsvFileManager4().read('test_data.csv')
  # list= CsvFileManager4().read('test_data.csv')
  #  print(list[0][0])
if __name__ == '__main__':
    list = CsvFileManager4().read('test_data.csv')
    print(list[1][0])