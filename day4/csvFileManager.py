#1.导入CSV代码库,是Python内置的代码库，如果是Excel文件需要下载响应的代码库：xlrd   1.通过命令下载，在dos窗口中输入pip install-U xlrd。也可以通过命令行在线安装：pip install-U selenium或者pip3 install selenium  -U是值升级到最新版的意思   pip是Python语言最常用的项目管理工具，和Java中的maven类似
#当Python2与Python3同时安装，那么pip要改为pip3
import csv
#2.点击file  点击settings  project小面的interpreter

path='C:/Users/51Testing/PycharmProjects/selenium7th/data/test_data.csv'
#1.每个反斜线后后面加一个反斜线 2.把每一个反斜线都改为正斜线
#print(path)
#3.打开路径对应的文件
file=open(path,'r')
#4.读取文件内容用CSV代码库  reader()方法是专门用来读取文件的
date_tabe=csv.reader(file)
#5.打印表中的每一行数据  item代表每一行，每循环一次就代表item里的最新的一行数据   data_table表示整个文件中的所有数据
for item in date_tabe:
    print(item)
