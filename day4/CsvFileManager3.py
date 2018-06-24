import csv
#每个测试用例对应着不同的CSV文件，每条测试用例都会打开一个CSV文件，所以每次也应该关闭该文件
class CsvFileManger3:
    @classmethod
    def read(self):
        path=r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file=open(path,'r')
        try:   #尝试执行一下代码
         #通过CSV代码库读取打开的CSV文件，获取文件中所有数据
          data_table=csv.reader(file)
          a=[1,2,3,4,5]
          a[7]
        #程序执行过程中是否报错，都能正常关闭打开的文件
          for item in data_table:
             print(item)
        finally: #无论程序是否有错，finally是最终结果
             file.close()   #方法最后应该天机close（）方法

if __name__ == '__main__':
    #csvr=CsvFileManger2()
    #csvr.read()
#方法上面加上@classmethod ，表示这个方法可以直接用类调用.. 不需要先实例化对象后才能调用
    CsvFileManger3.read()